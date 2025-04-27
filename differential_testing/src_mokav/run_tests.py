import logging
import os
import json
import re
from .code_runner import CodeRunner
import shutil
import hashlib
import asyncio

def load_file_as_string(file_path):
    """Load file content as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error loading file {file_path}: {e}")
        return None

def ensure_directory_exists(directory_path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def cleanup_temp_files(problem_dir_hash):
    """Remove temporary files used by CodeRunner."""
    temp_files = [
        f"output/temp/mokav/temp_acc_qb_{problem_dir_hash}.py", 
        f"output/temp/mokav/temp_bug_qb_{problem_dir_hash}.py", 
        f"output/temp/mokav/temp_test_case_{problem_dir_hash}.py",
        f"output/temp/mokav/temp_acc_exec_{problem_dir_hash}.py",
        f"output/temp/mokav/temp_bug_exec_{problem_dir_hash}.py"
    ]
    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)

def post_process_results(example_dir, mokav_dir, results_file):
    """Post-process test results to add detailed pass/fail counts and identify differing inputs."""
    try:
        with open(results_file, 'r') as f:
            results = json.load(f)
        
        passed_tests = 0
        failed_tests = 0
        error_tests = 0
        differing_inputs = []
        
        generated_tests_dir = os.path.join(mokav_dir, "generated_tests")
        if not os.path.exists(generated_tests_dir):
            return
        
        iteration_dirs = [d for d in os.listdir(generated_tests_dir) 
                         if os.path.isdir(os.path.join(generated_tests_dir, d)) and d.startswith("iteration_")]
        
        # Process each iteration
        for iteration_dir in iteration_dirs:
            iteration_path = os.path.join(generated_tests_dir, iteration_dir)
            output_file = os.path.join(iteration_path, "all_tests_output.txt")
            
            if not os.path.exists(output_file):
                continue
                
            # Read test output file
            with open(output_file, 'r') as f:
                output_content = f.read()
            
            fail_count = output_content.count("FAILED (failures=1)")
            error_count = output_content.count("FAILED (errors=1)")
            pass_count = output_content.count("OK")
            
            passed_tests += pass_count
            failed_tests += fail_count
            error_tests += error_count
            
            test_case_files = [f for f in os.listdir(iteration_path) 
                             if f.startswith("test_case_") and f.endswith(".py")]
            
            for test_file in test_case_files:
                test_path = os.path.join(iteration_path, test_file)
                with open(test_path, 'r') as f:
                    test_content = f.read()
                
                # test index
                test_index = test_file.split("_")[-1].split(".")[0]
                
                # Extract the input value from the test with regex
                input_match = re.search(r'input_\d+\s*=\s*"?([^"\n]+)"?', test_content)
                if not input_match:
                    # for lists
                    input_match = re.search(r'input_\d+\s*=\s*(\[[^\]]+\])', test_content)
                
                if input_match:
                    input_value = input_match.group(1)
                    
                    all_tests_file = os.path.join(iteration_path, "all_tests_output.txt")
                    if os.path.exists(all_tests_file):
                        with open(all_tests_file, 'r') as f:
                            all_tests_content = f.read()
                        
                        sections = all_tests_content.split("NEW TEST OUTPUT:")
                        for i, section in enumerate(sections):
                            if i == int(test_index) + 1:
                                # Only count AssertionError as a true difference, not general errors
                                if "AssertionError" in section:
                                    # Create a relative path to the test
                                    rel_path = os.path.join(example_dir, "mokav", "generated_tests", iteration_dir, test_file)
                                    
                                    # Extract the actual values from the assertion error if possible
                                    values_match = re.search(r'AssertionError: ([^\n]+)', section)
                                    values = values_match.group(1) if values_match else "Unknown difference"
                                    
                                    differing_inputs.append({
                                        "input": input_value,
                                        "test_file": rel_path,
                                        "values": values
                                    })
        
        # Calculate total tests including errors
        total_tests = passed_tests + failed_tests + error_tests
        
        if total_tests == 0:
            raw_count = results.get("total_tests", 0)
            if isinstance(raw_count, int) and raw_count > 0:
                total_tests = raw_count
        
        # Update the results
        results["total_tests"] = {
            "passed": passed_tests,
            "failed": failed_tests,
            "error": error_tests,
            "total": total_tests,
            "pass_rate": passed_tests / total_tests if total_tests > 0 else 0
        }
        
        if differing_inputs:
            results["differing_inputs"] = differing_inputs
        
        # Save updated results
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
            
        # logging.info(f"Post-processed results for {example_dir}: passed={passed_tests}, failed={failed_tests}, error={error_tests}, total={total_tests}")
        
    except Exception as e:
        logging.error(f"Error post-processing results for {example_dir}: {e}")

async def run_tests(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))  # Go up two levels
    examples_dir = os.path.join(root_dir, "output", "temp", "examples")
    problem_dir = os.path.join(examples_dir, eval_strategy, model_name, f"P{problem_id}_V{version_id}_{anonymous}")
    
    #create hash for problem_dir
    problem_dir_hash = hashlib.sha256(problem_dir.encode()).hexdigest()
    
    # logging.info(f"Root directory: {root_dir}")
    # logging.info(f"Examples directory: {examples_dir}")
    
    generated_tests_dir = os.path.join(script_dir, 'generated_tests')
    #if generated tests dir exists, remove it by force
    # print("GENERATED_TESTS", generated_tests_dir, '\n\n')
    # if os.path.exists(generated_tests_dir):
    #     shutil.rmtree(generated_tests_dir)

    ensure_directory_exists(generated_tests_dir)
    
    code_runner = CodeRunner(
        is_func=False,
        is_qb=True, 
        iteration_count=1, 
        meta_data_config='BADTIE', 
        generated_tests_dir=generated_tests_dir,
        number_of_samples=10,
        temperature=1, 
        problem_dir_hash=problem_dir_hash
    )

    example_dirs = [problem_dir]
    for example_dir in sorted(example_dirs):
        example_path = os.path.join(examples_dir, example_dir)
        # logging.info(f"Processing {example_dir}...")
        
        # Paths for correct and incorrect code files
        correct_file = os.path.join(example_path, "correct.py")
        incorrect_file = os.path.join(example_path, "incorrect.py")
        
        if not os.path.exists(correct_file) or not os.path.exists(incorrect_file):
            logging.warning(f"Skipping {example_dir}: missing correct.py or incorrect.py")
            continue
        
        # Load code as strings
        correct_code = load_file_as_string(correct_file)
        incorrect_code = load_file_as_string(incorrect_file)
        
        if not correct_code or not incorrect_code:
            logging.warning(f"Skipping {example_dir}: failed to load code files")
            continue
        
        existing_test = {'inputdata': ''}
        
        
        # logging.info(f"Using test input: {existing_test['inputdata']}")
            

        
        try:
            mokav_dir = os.path.join(example_path, "mokav")
            ensure_directory_exists(mokav_dir)
            
            generated_tests_dir_for_example = os.path.join(mokav_dir, "generated_tests")
            if os.path.exists(generated_tests_dir_for_example):
                shutil.rmtree(generated_tests_dir_for_example)
            ensure_directory_exists(generated_tests_dir_for_example)
            
            results_dir = os.path.join(mokav_dir, "results")
            ensure_directory_exists(results_dir)
            
            # Set the save directory for generated tests
            code_runner.example_save_dir = generated_tests_dir_for_example
            # print("GENERATED_TESTS", generated_tests_dir_for_example, '\n\n')
            
            # Run the test
            result = await code_runner.check_test(
                acc1=correct_code,
                rej=incorrect_code,
                existing_test=existing_test,
                problem_id=example_dir,
                author_id=example_dir
            )
            
            # logging.info(f"{example_dir} result: {result}")
            
            result_file = os.path.join(results_dir, "results.json")
            with open(result_file, 'w') as f:
                json.dump(result, f, indent=2)
            
            # Post-process the results
            post_process_results(example_dir, mokav_dir, result_file)
            
            # logging.info(f"Saved result to {result_file}")
            # logging.info(f"Generated tests saved to {generated_tests_dir_for_example}")
            
        except Exception as e:
            logging.error(f"Error processing {example_dir}: {e}")
    
    # logging.info("All examples processed")
    
    cleanup_temp_files(problem_dir_hash)
