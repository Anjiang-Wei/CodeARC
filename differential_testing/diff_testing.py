#!/usr/bin/env python3
"""
Comprehensive differential testing runner script.
Runs all steps of the differential testing process:
1. Generate tests with Pynguin
2. Run tests with Pynguin
3. Run tests with Mokav
4. Compile results from both tools
"""

import os
import subprocess
import json
import time
import asyncio
from .src_pynguin.generate_tests import generate_tests as pynguin_generate_tests
from .src_pynguin.run_tests import run_tests as pynguin_run_tests
from .src_mokav.run_tests import run_tests as mokav_run_tests

def run_command(cmd, verbose=True):
    if verbose:
        pass
        # print(f"Running: {cmd}")
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print(f"Subprocess run_command1, {elapsed_time}, {cmd}")
        
        if result.returncode != 0:
            # print(f"Error running command: {cmd}")
            # print(f"Error: {result.stderr}")
            return False, result.stderr
        
        return True, result.stdout
    except subprocess.TimeoutExpired:
        # print(f"Command timed out: {cmd}")
        return False, "Command timed out after 5 seconds"
    except Exception as e:
        # print(f"Exception running command: {cmd}")
        # print(f"Error: {str(e)}")
        return False, str(e)

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def run_pynguin_generation(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    # print("\n===== Running Pynguin Test Generation =====")
    pynguin_generate_tests(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    # print("Pynguin test generation completed successfully")

def run_pynguin_tests(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    """run tsts with Pynguin"""
    # print("\n===== Running Pynguin Tests =====")
    pynguin_run_tests(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    # print("Pynguin test execution completed successfully")

async def run_mokav_tests(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    """Run tests with Mokav"""
    # print("\n===== Running Mokav Tests =====")
    await mokav_run_tests(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    # print("Mokav test execution completed successfully")

def run_rename():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    run_script = os.path.join(script_dir, "rename.py")
    
    # exec
    os.chmod(run_script, 0o755)
    
    cmd = f"python {run_script}"
    success, output = run_command(cmd)
    
    return success

def compile_result(eval_strategy: str, model_name: str, problem_id: int, version_id: str, anonymous: bool):
    """Compile results from both tools"""
    # print("\n===== Compiling Results =====")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(script_dir, os.pardir, "output/temp/examples")
    example_dir =  os.path.join(examples_dir, eval_strategy, model_name, f"P{problem_id}_V{version_id}_{anonymous}")
    
    # Create output directory for combined results
    combined_result_dir = os.path.join(example_dir, "combined_result")
    ensure_directory_exists(combined_result_dir)
    
    all_results = []
    
    example_dirs = [example_dir]
    for example_dir in example_dirs:        
        example_result = {
            "problem_id": problem_id,
            "version_id": version_id,
            "example":  os.path.abspath(example_dir)
        }
        
        pynguin_results_path = os.path.join(example_dir, "pynguin", "results", "results.json")
        if os.path.exists(pynguin_results_path):
            try:
                with open(pynguin_results_path, 'r') as f:
                    pynguin_results = json.load(f)
                
                # Keep fields important
                example_result["pynguin"] = {
                    "Tool": pynguin_results.get("Tool", "Pynguin"),
                    "Equivalent": pynguin_results.get("Equivalent", None),
                    "total_tests": pynguin_results.get("total_tests", None),
                    "differing_test_files": pynguin_results.get("differing_test_files", [])
                }
                
                # print(f"Loaded Pynguin results for {example_dir_name}")
            except Exception as e:
                pass
                # print(f"Error loading Pynguin results for {example_dir_name}: {e}")
        else:
            pass
            # print(f"No Pynguin results found for {example_dir_name}")
        
        # Get Mokav results
        mokav_results_path = os.path.join(example_dir, "mokav", "results", "results.json")
        if os.path.exists(mokav_results_path):
            try:
                with open(mokav_results_path, 'r') as f:
                    mokav_results = json.load(f)
                
                example_result["mokav"] = {
                    "Tool": mokav_results.get("Tool", "Mokav"),
                    "Equivalent": mokav_results.get("Equivalent", None),
                    "total_tests": mokav_results.get("total_tests", None),
                    "differing_inputs": mokav_results.get("differing_inputs", [])
                }
                
                # print(f"Loaded Mokav results for {example_dir_name}")
            except Exception as e:
                example_result["mokav"] = {
                    "Tool": "Mokav",
                    "Equivalent": None,
                    "total_tests": None,
                    "differing_inputs": []
                }
                # print(f"Error loading Mokav results for {example_dir_name}: {e}")
        else:
            example_result["mokav"] = {
                    "Tool": "Mokav",
                    "Equivalent": None,
                    "total_tests": None,
                    "differing_inputs": []
                }
            # print(f"No Mokav results found for {example_dir_name}")
        
        all_results.append(example_result)
    
    combined_results_path = os.path.join(combined_result_dir, "combined_result.json")
    with open(combined_results_path, 'w') as f:
        json.dump(all_results[0], f, indent=2)
    
    # print(f"Combined results saved to {combined_results_path}")
    
    summary_path = os.path.join(combined_result_dir, "summary.txt")
    with open(summary_path, 'w') as f:
        f.write("Differential Testing Summary\n")
        f.write("==========================\n\n")
        
        for result in all_results:
            example = result["example"]
            pynguin = result["pynguin"]
            mokav = result["mokav"]
            
            f.write(f"Example: {example}\n")
            f.write("-" * (len(example) + 9) + "\n\n")
            
            # Pynguin summary
            f.write("Pynguin:\n")
            if pynguin:
                if "Equivalent" in pynguin:
                    f.write(f"  Equivalent implementations: {pynguin['Equivalent']}\n")
                
                if "total_tests" in pynguin:
                    total = pynguin["total_tests"]
                    if total is not None and type(total) is dict:
                        f.write(f"  Tests: {total['passed']}/{total['total']} passed ")
                        f.write(f"({total['pass_rate']:.2%} pass rate)\n")
                
                if "differing_test_files" in pynguin:
                    f.write(f"  Differing tests: {len(pynguin['differing_test_files'])}\n")
                    for test in pynguin['differing_test_files']:
                        f.write(f"    - {test}\n")
            else:
                f.write("  No results available\n")
            
            # Mokav summary
            f.write("\nMokav:\n")
            if mokav:
                # Extract key results
                if "Equivalent" in mokav:
                    f.write(f"  Equivalent implementations: {mokav['Equivalent']}\n")
                
                if "total_tests" in mokav:
                    total = mokav["total_tests"]
                    if total is not None and type(total) is dict:
                        f.write(f"  Tests: {total['passed']}/{total['total']} passed ")
                        f.write(f"({total['pass_rate']:.2%} pass rate)\n")
                
                if "differing_inputs" in mokav:
                    f.write(f"  Differing inputs: {len(mokav['differing_inputs'])}\n")
                    for diff in mokav['differing_inputs']:
                        f.write(f"    - Input: {diff['input']}\n")
                        f.write(f"      File: {diff['test_file']}\n")
                        if 'values' in diff:
                            f.write(f"      Values: {diff['values']}\n")
            else:
                f.write("  No results available\n")
            
            f.write("\n\n")
    
    # print(f"Summary saved to {summary_path}")
    
    return all_results[0]

async def test(eval_strategy: str, model_name: str, problem_id: str, version_id: str, anonymous: bool):
    start_time = time.time()
    run_rename()
    # print("Starting comprehensive differential testing...")
    
    run_pynguin_generation(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    pg_end_time = time.time()
    run_pynguin_tests(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    pg_test_end_time = time.time()

    await run_mokav_tests(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    mokav_end_time = time.time()

    result = compile_result(eval_strategy=eval_strategy, model_name=model_name, problem_id=problem_id, version_id=version_id, anonymous=anonymous)
    
    # Print summary
    # print("\n===== Differential Testing Complete =====")
    # print(f"Total time: {time.time() - start_time:.2f} seconds") 
    # print(f"Pynguin generation time: {pg_end_time - start_time:.2f} seconds")
    # print(f"Pynguin testing time: {pg_test_end_time - pg_end_time:.2f} seconds")
    # print(f"Mokav testing time: {mokav_end_time - pg_test_end_time:.2f} seconds")
    # print(f"Pynguin generation: {'Success' if pynguin_gen else 'Failed'}")
    # print(f"Pynguin testing: {'Success' if pynguin_test else 'Failed'}")
    # print(f"Mokav testing: {'Success' if mokav_test else 'Failed'}")
    # print(f"Total examples processed: {len(result)}")
    
    # location for rsults
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # print(os.pardir)
    results_path = os.path.join(script_dir, os.pardir, "output", "temp", "examples", f"P{problem_id}_V{version_id}_{anonymous}", "combined_result", "combined_results.json")
    summary_path = os.path.join(script_dir, os.pardir, "output", "temp", "examples", f"P{problem_id}_V{version_id}_{anonymous}", "combined_result", "summary.txt")
    
    # print(f"\nResults saved to:")
    # print(f"  - {results_path}")
    # print(f"  - {summary_path}")

    return result
