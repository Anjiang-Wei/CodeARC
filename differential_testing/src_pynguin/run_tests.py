#!/usr/bin/env python3
"""
Run generated tests against both correct and incorrect implementations
"""

import os
import sys
import subprocess
import glob
import csv
import json
from pathlib import Path
import time

def extract_test_results(output):
    """Extract test results from pytest output"""
    passed = 0
    failed = 0
    
    for line in output.split('\n'):
        if "PASSED [" in line:
            passed += 1
        elif "FAILED [" in line:
            failed += 1
    
    return {
        'passed': passed,
        'failed': failed
    }

def run_test(test_file, program_file, implementation_code, example_dir_name, verbose=True):
    """Run a single test against an implementation"""
    with open(program_file, 'w') as f:
        f.write(implementation_code)
    
    # Run the test with pytest
    cmd = ["pytest", test_file, "-v"]
    start_time = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except subprocess.TimeoutExpired:
        return {
            'results': {'passed': 0, 'failed': 0},
            'output': "Command timed out after 5 seconds",
            'test_file': None
        }
    except Exception as e:
        return {
            'results': {'passed': 0, 'failed': 0},
            'output': str(e),
            'test_file': None
        }
    end_time = time.time()
    elapsed_time = end_time - start_time
    # print(f"Subprocess run_command3, {elapsed_time}, {cmd}")

    test_results = extract_test_results(result.stdout)
    
    relative_path = None
    if test_results['failed'] > 0:
        # Get the path from example#/ onwards
        parts = test_file.split(example_dir_name)
        if len(parts) > 1:
            relative_path = example_dir_name + parts[1]
    
    if verbose:
        pass
        # print(f"  - Passed: {test_results['passed']}, Failed: {test_results['failed']}")
    
    return {
        'results': test_results,
        'output': result.stdout,
        'test_file': relative_path
    }

def run_tests(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    diff_testing_dir = os.path.dirname(script_dir)    
    examples_dir = os.path.join(os.path.dirname(diff_testing_dir), "output", "temp", "examples")
    problem_dir = os.path.join(examples_dir, eval_strategy, model_name, f"P{problem_id}_V{version_id}_{anonymous}")
    example_dirs = [problem_dir]

    if not os.path.exists(examples_dir):
        print(f"Error: Examples directory not found at {examples_dir}")
        return
    

    summary = []
    
    # For each example directory, run tests
    for example_dir_name in example_dirs:
        example_dir_path = os.path.join(examples_dir, example_dir_name)
        pynguin_dir = os.path.join(example_dir_path, "pynguin")
        

        results_dir = os.path.join(pynguin_dir, "results")
        os.makedirs(results_dir, exist_ok=True)
        
        # Define paths
        correct_file = os.path.join(example_dir_path, "correct.py")
        incorrect_file = os.path.join(example_dir_path, "incorrect.py")
        
        if not (os.path.exists(correct_file) and os.path.exists(incorrect_file)):
            print(f"Skipping {example_dir_name}: Missing implementation files")
            continue
        
        # print(f"Testing {example_dir_name} (correct vs incorrect):")
        

        with open(correct_file, 'r') as f:
            correct_code = f.read()
        
        with open(incorrect_file, 'r') as f:
            incorrect_code = f.read()
        
        module_results = {
            "Tool": "Pynguin"
        }
        
        total_passed = 0
        total_tests = 0
        differing_test_files = []
        

        correct_test_dir = os.path.join(pynguin_dir, "correct")
        correct_test_file = os.path.join(correct_test_dir, "test_transformed_correct.py")
        correct_program_file = os.path.join(correct_test_dir, "correct.py")
        
        if os.path.exists(correct_test_file):
            # print(f"Running tests from {correct_test_file}:")
            
            # Test with incorrect implementation on correct tests
            # print("  Against incorrect implementation:")
            incorrect_on_correct = run_test(correct_test_file, correct_program_file, incorrect_code, example_dir_name)
            
            # Save test output
            with open(os.path.join(results_dir, "incorrect_on_correct.log"), 'w') as f:
                f.write(incorrect_on_correct['output'])
            

            incorrect_pass = incorrect_on_correct['results']['passed']
            incorrect_fail = incorrect_on_correct['results']['failed']
            total_passed += incorrect_pass
            total_tests += (incorrect_pass + incorrect_fail)
            
            # Save failing test file if any tests failed
            if incorrect_on_correct['test_file']:
                differing_test_files.append(incorrect_on_correct['test_file'])
            
            module_results['incorrect_on_correct'] = incorrect_on_correct['results']
        
        # Run tests generated for incorrect implementation
        incorrect_test_dir = os.path.join(pynguin_dir, "incorrect")
        incorrect_test_file = os.path.join(incorrect_test_dir, "test_transformed_incorrect.py")
        incorrect_program_file = os.path.join(incorrect_test_dir, "incorrect.py")
        
        if os.path.exists(incorrect_test_file):
            # print(f"Running tests from {incorrect_test_file}:")

            # print("  Against correct implementation:")
            correct_on_incorrect = run_test(incorrect_test_file, incorrect_program_file, correct_code, example_dir_name)
            
            # Save test output
            with open(os.path.join(results_dir, "correct_on_incorrect.log"), 'w') as f:
                f.write(correct_on_incorrect['output'])
            
            correct_pass = correct_on_incorrect['results']['passed']
            correct_fail = correct_on_incorrect['results']['failed']
            total_passed += correct_pass
            total_tests += (correct_pass + correct_fail)
            
            # Save failing test file if any tests failed
            if correct_on_incorrect['test_file']:
                differing_test_files.append(correct_on_incorrect['test_file'])
            
            module_results['correct_on_incorrect'] = correct_on_incorrect['results']
        
        module_results['Equivalent'] = True # Default to True, will be updated later if needed

        if 'incorrect_on_correct' in module_results and 'correct_on_incorrect' in module_results:
            # For implementations to be equivalent, all tests must pass on both implementations
            total_failures = (module_results['incorrect_on_correct']['failed'] + 
                             module_results['correct_on_incorrect']['failed'])
            equivalent = total_failures == 0
            
            module_results['Equivalent'] = equivalent
        
        module_results['total_tests'] = {
            'passed': total_passed,
            'total': total_tests,
            'pass_rate': total_passed / total_tests if total_tests > 0 else 0
        }
        
        if differing_test_files:
            module_results['differing_test_files'] = differing_test_files
        
        summary.append({
            'example': example_dir_name,
            'results': module_results
        })
        
        with open(os.path.join(results_dir, "results.json"), 'w') as f:
            json.dump(module_results, f, indent=2)
    
    combined_results_path = Path(examples_dir) / eval_strategy / model_name / f"P{problem_id}_V{version_id}_{anonymous}" / "combined_result"
    combined_results_path.mkdir(parents=True, exist_ok=True)
    summary_path = combined_results_path / "summary.csv"
    with open(summary_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Example',
            'Tool',
            'Incorrect on Correct',
            'Correct on Incorrect',
            'Total Pass Rate',
            'Equivalent'
        ])
        
        for item in summary:
            results = item['results']
            row = [item['example'], results.get('Tool', 'N/A')]
            
            # Incorrect on Correct results
            if 'incorrect_on_correct' in results:
                incorrect_on_correct = results['incorrect_on_correct']
                total = incorrect_on_correct['passed'] + incorrect_on_correct['failed']
                row.append(f"{incorrect_on_correct['passed']}/{total}")
            else:
                row.append('N/A')
            
            # Correct on Incorrect results
            if 'correct_on_incorrect' in results:
                correct_on_incorrect = results['correct_on_incorrect']
                total = correct_on_incorrect['passed'] + correct_on_incorrect['failed']
                row.append(f"{correct_on_incorrect['passed']}/{total}")
            else:
                row.append('N/A')
            
            # Total pass rate
            if 'total_tests' in results:
                total_tests = results['total_tests']
                row.append(f"{total_tests['passed']}/{total_tests['total']}")
            else:
                row.append('N/A')
            
            # Equivalent
            row.append(str(results.get('Equivalent', 'N/A')))
            
            writer.writerow(row)
    
    # print("\nTest execution complete!")
    # print(f"Summary CSV saved to: {summary_path}")
    # print("Detailed results saved to each example's pynguin/results directory")
 
