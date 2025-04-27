#!/usr/bin/env python3
import subprocess
import argparse
import time

def parse_args():
    parser = argparse.ArgumentParser(description='Run evaluation with configurable parameters')
    parser.add_argument('--model_name', type=str, 
                        default='openai/gpt-4o-mini',
                        help='Model name to evaluate')
    parser.add_argument('--timeout', type=str, default='6m',
                        help='Timeout for each evaluation run (e.g., 6m, 10s)')
    parser.add_argument('--total_idx', type=int, default=1114,
                        help='Total number of problems to evaluate')
    parser.add_argument('--num_processes', type=int, default=20,
                        help='Number of processes to use for evaluation')
    parser.add_argument('--datasets', type=str, default='anonymous,annotated',
                        help='Comma-separated list of datasets to evaluate')
    parser.add_argument('--evaluation_strategy', type=str, default='reasoning_guided',
                        help='Evaluation strategy to use')
    parser.add_argument('--max_debug_rounds', type=int, default=None,
                        help='Maximum number of debug rounds (optional)')
    parser.add_argument('--max_invocations', type=int, default=None,
                        help='Maximum number of invocations (optional)')
    parser.add_argument('--max_tries', type=int, default=None,
                        help='Maximum number of tries (optional)')
    return parser.parse_args()

def convert_timeout_to_seconds(timeout_str):
    """Convert timeout string (like '6m' or '10s') to seconds."""
    unit = timeout_str[-1].lower()
    value = int(timeout_str[:-1])
    
    if unit == 's':
        return value
    elif unit == 'm':
        return value * 60
    else:
        raise ValueError(f"Unsupported timeout unit: {unit}. Only 's' (seconds) and 'm' (minutes) are supported.")

def run_evaluation(args):
    model_name = args.model_name
    timeout_seconds = convert_timeout_to_seconds(args.timeout)
    total_idx = args.total_idx
    num_processes = args.num_processes
    datasets = args.datasets.split(',')
    
    i = 0
    while i < total_idx:
        for dataset in datasets:
            print(f"Evaluating {model_name} on {dataset} from {i} to {i+num_processes} in parallel. Evaluation will skip if the results already exist.")
            
            cmd = [
                "python", "src/evaluate.py",
                "--model_names", model_name,
                "--datasets", dataset,
                "--evaluation_strategy", args.evaluation_strategy,
                "--num_processes", str(num_processes),
                "--start_idx", str(i),
                "--end_idx", str(i+num_processes)
            ]
            
            # Add optional arguments if provided
            if args.max_debug_rounds is not None:
                cmd.extend(["--max_debug_rounds", str(args.max_debug_rounds)])
            if args.max_invocations is not None:
                cmd.extend(["--max_invocations", str(args.max_invocations)])
            if args.max_tries is not None:
                cmd.extend(["--max_tries", str(args.max_tries)])
            
            try:
                process = subprocess.Popen(cmd)
                
                # Set a timeout
                start_time = time.time()
                while process.poll() is None:
                    if time.time() - start_time > timeout_seconds:
                        process.terminate()
                        try:
                            process.wait(timeout=5)  # Give it 5 seconds to terminate gracefully
                        except subprocess.TimeoutExpired:
                            process.kill()  # Force kill if it doesn't terminate
                        print("The command timed out.")
                        break
                    time.sleep(0.1)
                
                exit_code = process.returncode
                if exit_code == 0:
                    print("The command completed successfully. Check results in output/evaluation_results")
                else:
                    print(f"The command exited with exit code {exit_code}.")
                
            except Exception as e:
                print(f"Error running evaluation: {e}")
            
            time.sleep(3)
        
        i += num_processes

def main():
    args = parse_args()
    run_evaluation(args)

if __name__ == "__main__":
    main()



