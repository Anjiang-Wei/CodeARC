#!/usr/bin/env python3
"""
Generate Pynguin tests for all example directories
Script location: diff_testing/src_pynguin/
Examples location: same level as diff_testing/
"""

import os
import sys
import subprocess
import glob
from pathlib import Path
import time

def run_pynguin(module_path, output_path, module_name, timeout=5, assertion_generation="SIMPLE", verbose=True):
    """Run Pynguin on a single module"""
    # Create directory structure
    os.makedirs(output_path, exist_ok=True)
    
    # Copy the module file to the output directory
    with open(f"{module_path}/{module_name}.py", 'r') as source:
        with open(f"{output_path}/{module_name}.py", 'w') as target:
            target.write(source.read())
    
    # Build the pynguin command
    cmd = (
        f"PYNGUIN_DANGER_AWARE=TRUE pynguin "
        f"--maximum-search-time {timeout} "
        f"--project-path {output_path} "
        f"--output-path {output_path} "
        f"--module-name {module_name} "
        f"--assertion-generation {assertion_generation}"
    )
    
    if verbose:
        pass
        # print(f"Running: {cmd}")
    
    # Execute the command
    start_time = time.time()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print(f"Subprocess run_command4, {elapsed_time}, {cmd}")

        if result.returncode != 0:
            # print(f"Error running Pynguin for {module_name}:")
            # print(result.stderr)
            return False
        
        if verbose:
            pass
            # print(f"Successfully generated tests for {module_name}")
        
        return True
    except subprocess.TimeoutExpired:
        # print(f"Timeout expired running Pynguin for {module_name}")
        return False
    except Exception as e:
        # print(f"Exception running Pynguin for {module_name}: {str(e)}")
        return False

def transform_xfail_tests(test_file_path):
    """Transform xfail tests to normal tests with commented out problematic lines"""
    output_path = test_file_path.replace('test_', 'test_transformed_')
    
    with open(test_file_path, 'r') as input_file:
        with open(output_path, 'w') as output_file:
            is_xfail = False
            lines = input_file.readlines()
            
            for i, line in enumerate(lines):
                if "xfail" in line:
                    # Comment out the xfail line
                    is_xfail = True
                    output_file.write('#' + line)
                else:
                    if is_xfail:
                        # Check if we're at the end of the xfail block
                        if i == len(lines) - 1 or lines[i + 1] == "\n":
                            output_file.write('#' + line)
                            is_xfail = False
                        # Check if this is a function definition line
                        elif (i == len(lines) - 2 or lines[i + 2] == '\n') and line.startswith("def "):
                            output_file.write('#' + line)
                        else:
                            output_file.write(line)
                    else:
                        output_file.write(line)
    
    return output_path

def generate_tests(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    diff_testing_dir = os.path.dirname(script_dir)
    examples_dir = os.path.join(os.path.dirname(diff_testing_dir), "output", "temp", "examples")
    problem_dir = os.path.join(examples_dir, eval_strategy, model_name, f"P{problem_id}_V{version_id}_{anonymous}")
    example_dirs = [problem_dir]
    
    # Process each example directory
    for example_dir_name in example_dirs:
        example_dir_path = os.path.join(examples_dir, example_dir_name)

        pynguin_dir = os.path.join(example_dir_path, "pynguin")
        os.makedirs(pynguin_dir, exist_ok=True)
        
        # Process correct.py
        if os.path.exists(os.path.join(example_dir_path, "correct.py")):
            # print(f"Processing {example_dir_name}/correct.py...")
            correct_output_dir = os.path.join(pynguin_dir, "correct")
            success = run_pynguin(example_dir_path, correct_output_dir, "correct")
            
            if success:
                # Transform xfail tests
                test_file = os.path.join(correct_output_dir, "test_correct.py")
                if os.path.exists(test_file):
                    transformed_file = transform_xfail_tests(test_file)
                    # print(f"Transformed tests saved to {transformed_file}")
                else:
                    pass
                    # print(f"Warning: Test file not found at {test_file}")
        
        # Process incorrect.py
        if os.path.exists(os.path.join(example_dir_path, "incorrect.py")):
            # print(f"Processing {example_dir_name}/incorrect.py...")
            incorrect_output_dir = os.path.join(pynguin_dir, "incorrect")
            success = run_pynguin(example_dir_path, incorrect_output_dir, "incorrect")
            
            if success:
                # Transform xfail tests
                test_file = os.path.join(incorrect_output_dir, "test_incorrect.py")
                if os.path.exists(test_file):
                    transformed_file = transform_xfail_tests(test_file)
                    # print(f"Transformed tests saved to {transformed_file}")
                else:
                    pass
                    # print(f"Warning: Test file not found at {test_file}")
    
    # print("\nTest generation complete!")
