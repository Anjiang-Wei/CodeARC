from utils import read_dataset_files
from invocators import ReasoningGuidedInvocator, SFTDistillation
from typing import List, Tuple, Dict
import argparse
import os
import json
from pathlib import Path
import asyncio
import multiprocessing
import time

def load_invocations(dataset: str, prompt_invocations_type: str, num_invocations: int, sft_distillation: bool = False):
    input_invocations = []
    output_invocations = []
    errored_invocations = []
    
    if sft_distillation:
        prompt_invocations_path = f"prompt_invocations/sft/{dataset}/num_invocations={num_invocations}/{prompt_invocations_type}/invocations.json"
    else:
        prompt_invocations_path = f"prompt_invocations/{dataset}/num_invocations={num_invocations}/{prompt_invocations_type}/invocations.json"
    
    with open(prompt_invocations_path, "r") as f:
        data = json.load(f) 
    
    sorted_data = sorted(data.items(), key=lambda x: int(x[0]))
    
    for key, value in sorted_data:
        sorted_idxs = sorted(value.items(), key=lambda x: int(x[0]))
        input_invocations.append([])
        output_invocations.append([])
        errored_invocations.append([])
        
        for idx, vv in sorted_idxs:
            input_invocations[-1].append(vv["input"])
            output_invocations[-1].append(vv["output"])
            errored_invocations[-1].append(vv["errored"])
        
    return input_invocations, output_invocations, errored_invocations

async def async_worker_fn(worker_input):
    """Original async worker function."""
    model_name, anonymous, input_invocations, output_invocations, prob_idx, gt_function, args = worker_input

    # Initialize default values to guarantee the file is written even on errors.
    is_correct = None
    results_trace = None
    conversation_history = None

    dataset_name = "anonymous" if anonymous else "annotated"
    if args.evaluation_strategy == "sft_distillation":
        problem_dir = f"{args.output_dir}/{dataset_name}/{args.evaluation_strategy}/{model_name}/max-invocations={args.max_invocations}_num-invocations-per-round={args.num_invocations_per_round}_max-debug-rounds={args.max_debug_rounds}_max-tries={args.max_tries}"
    else:
        eval_strategy = f'reasoning_guided_mi={args.max_invocations}_mdr={args.max_debug_rounds}'
        problem_dir = os.path.join(args.output_dir, dataset_name, eval_strategy, model_name)
    if not os.path.exists(problem_dir):
        os.makedirs(problem_dir, exist_ok=True)
    output_path = f"{problem_dir}/{prob_idx}.json"

    if os.path.exists(output_path):
        return None

    invocator_cls = SFTDistillation if args.evaluation_strategy == "sft_distillation" else ReasoningGuidedInvocator
    invocator = invocator_cls(
        model_name=model_name, 
        prompt_path=args.prompt_path, 
        max_invocations=args.max_invocations, 
        max_debug_rounds=args.max_debug_rounds,
        max_tries=args.max_tries, 
        anonymous=anonymous
    )

    try:
        is_correct, results_trace, conversation_history = await invocator(
            input_invocations, output_invocations, prob_idx, gt_function
        )
    except asyncio.CancelledError:
        print(f"Worker {prob_idx} cancelled.")
        raise
    except Exception as e:
        print(f"Exception occurred in worker {prob_idx}: {e}")
    finally:
        with open(output_path, "w") as f:
            json.dump({
                "is_correct": is_correct, 
                "results_trace": results_trace, 
                "conversation_history": conversation_history
            }, f)

    return is_correct

def blocking_worker_fn(worker_input):
    """
    A synchronous wrapper that runs async_worker_fn in its own event loop.
    This avoids blocking the main event loop if async_worker_fn does CPU or blocking tasks.
    """
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(async_worker_fn(worker_input))
    finally:
        loop.close()

async def worker_wrapper(worker_input, semaphore, timeout):
    """
    Offload the blocking_worker_fn to a separate thread via asyncio.to_thread,
    ensuring the main event loop isn't blocked by the invocation logic.
    """
    # Manually acquire and release semaphore so we can control concurrency.
    await semaphore.acquire()
    try:
        return await asyncio.wait_for(
            asyncio.to_thread(blocking_worker_fn, worker_input),
            timeout
        )
    except asyncio.TimeoutError:
        print(f"Task {worker_input[-2]} timed out after {timeout} seconds.")
        return None
    except Exception as e:
        print(f"Task {worker_input[-2]} raised an exception: {e}")
        return None
    finally:
        semaphore.release()

async def main_async(args):
    """Main async function with controlled concurrency."""
    if args.evaluation_strategy == "sft_distillation": 
        args.max_debug_rounds = 0
    
    Path(args.output_dir).mkdir(parents=True, exist_ok=True) 
    start_time = time.time()

    # Determine the overall code count and task count.
    if args.end_idx is None:
        overall_end_idx = 1114
    else:
        overall_end_idx = args.end_idx
    code_count = overall_end_idx - args.start_idx
    task_count = code_count * len(args.datasets) * len(args.model_names)
    
    max_parallel_tasks = min(args.num_processes or multiprocessing.cpu_count(), task_count) + 2
    semaphore = asyncio.Semaphore(max_parallel_tasks) 

    print(f"Running with {max_parallel_tasks} parallel tasks using asyncio + threads (to_thread).")

    tasks = []
    is_sft_distillation = args.evaluation_strategy == "sft_distillation"
    for dataset in args.datasets:
        code_strings = read_dataset_files(dataset, is_sft_distillation)
        # Use a per-dataset end index without modifying args.end_idx globally.
        end_idx_dataset = len(code_strings) if args.end_idx is None else args.end_idx
        code_strings = code_strings[args.start_idx:end_idx_dataset]
        input_invocations, output_invocations, errored_invocations = load_invocations(
            dataset, args.prompt_invocations_type, args.num_invocations_per_round, is_sft_distillation
        )
        for model_name in args.model_names:
            worker_inputs = [
                (
                    model_name, 
                    dataset == "anonymous", 
                    input_invocations[prob_idx + args.start_idx], 
                    output_invocations[prob_idx + args.start_idx], 
                    prob_idx + args.start_idx, 
                    gt_function, 
                    args
                )
                for prob_idx, gt_function in enumerate(code_strings)
            ]
            for worker_input in worker_inputs:
                # Multiply the timeout (in minutes) by 60 to convert it to seconds.
                tasks.append(worker_wrapper(worker_input, semaphore, timeout=args.timeout * 60))

    results = await asyncio.gather(*tasks, return_exceptions=True)
    results = [r for r in results if r is not None]

    total_correct = sum(1 for r in results if r)
    final_accuracy = total_correct / len(tasks) if tasks else 0
    print(f"problem_ids=[{args.start_idx}:{overall_end_idx}], datasets={args.datasets}, model_names={args.model_names}, "
          f"Final accuracy: {final_accuracy:.2%} ({total_correct}/{len(tasks)}), Total time: {time.time() - start_time:.2f} seconds")

def main(args):
    """Wrapper for running the async main function."""
    # Remove any temp/cache files if present.
    [os.remove(fl) for fl in os.listdir('.') if fl.startswith('temp_') and fl.endswith('.py')]
    [os.remove(fl) for fl in os.listdir('.') if fl.startswith('cache_') and fl.endswith('.json')]
    
    asyncio.run(main_async(args))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # general arguments
    parser.add_argument("--model_names", nargs="+", type=str, default=["openai/gpt-4o-mini"])
    parser.add_argument("--datasets", nargs="+", default=["anonymous", "annotated"])
    parser.add_argument("--prompt_invocations_type", type=str, default="llm", choices=["llm", "tc-generated"])
    
    # evaluation arguments
    parser.add_argument("--evaluation_strategy", type=str, default="reasoning_guided", choices=["reasoning_guided", "sft_distillation"])
    parser.add_argument("--start_idx", type=int, default=0)
    parser.add_argument("--end_idx", type=int, default=None)
    
    # pipeline arguments
    parser.add_argument("--max_invocations", type=int, default=30)
    parser.add_argument("--num_invocations_per_round", type=int, default=10)
    parser.add_argument("--max_debug_rounds", type=int, default=1)
    parser.add_argument("--max_tries", type=int, default=2)
    parser.add_argument("--prompt_path", type=str, default="./prompts.yaml")

    # saving arguments
    parser.add_argument("--output_dir", type=str, default="output/evaluation_results")
    parser.add_argument("--overwrite", type=bool, default=False)
    
    # parallelism control
    parser.add_argument("--num_processes", type=int, default=None, 
                       help="Number of processes to use for parallelism. Defaults to number of CPU cores.")
    
    # Timeout argument (in minutes)
    parser.add_argument("--timeout", type=int, default=5, 
                        help="Timeout for each thread in minutes (default: 5 minutes).")

    args = parser.parse_args()

    main(args)
