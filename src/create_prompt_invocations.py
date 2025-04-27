import pandas as pd
import os
import re
from tqdm import tqdm
import fire
from utils import extract_function_names, read_dataset_files, clean_code, process_model_invocations
from typing import List, Tuple, Dict, Set, Optional, Union, Any
import io
import sys
import contextlib
import inspect
import ast
import math
import cmath
import random
import itertools
import collections
import heapq
from collections import defaultdict, Counter, deque, OrderedDict
import string
import datetime
import json
import functools
import copy
import bisect
from utils import local_executor
from pathlib import Path
import openai
from openai import OpenAI
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed


def create_prompt_invocations_from_existing_test_cases(num_invocations: int, code_strings: list, function_names: list):
    # Get code strings from parquet file
    test_cases = pd.read_parquet("dataset.parquet")['code'].tolist()

    test_codes = [test_code + f'\ndat = gen1({num_invocations})' for test_code in test_cases]
    
    input_invocations = []
    output_invocations = []
    errored_lst = []
    
    error_count = 0  # Replace unused set with a counter

    for i, test_code in tqdm(enumerate(test_codes), desc = "Creating prompt innocations", colour = "green"):
        namespace = {}
        exec(test_code, namespace)
        test_values = namespace['dat']
        
        input_invocations.append([]) 
        output_invocations.append([])
        errored_lst.append([])
        
        for j in range(num_invocations):
            # Handle case where test_values[j] is a list
            if isinstance(test_values[j], list):
                args_list = []
                for val in test_values[j]:
                    if isinstance(val, (int, float)) and val < 0:
                        val = abs(val)  # Take absolute value of negative numbers
                    if isinstance(val, str):
                        args_list.append(repr(val))  # Use repr for proper string escaping
                    elif isinstance(val, list):
                        # Process nested lists for negative values
                        processed_list = [abs(v) if isinstance(v, (int, float)) and v < 0 else v for v in val]
                        args_list.append(repr(processed_list))
                    else:
                        args_list.append(str(val))
                args = ', '.join(args_list)
            # Handle case where test_values[j] is a dictionary
            elif isinstance(test_values[j], dict):
                args_list = []
                for val in test_values[j].values():
                    if isinstance(val, (int, float)) and val < 0:
                        val = abs(val)  # Take absolute value of negative numbers
                    if isinstance(val, str):
                        args_list.append(repr(val))  # Use repr for proper string escaping
                    elif isinstance(val, list):
                        # Process nested lists for negative values
                        processed_list = [abs(v) if isinstance(v, (int, float)) and v < 0 else v for v in val]
                        args_list.append(repr(processed_list))
                    else:
                        args_list.append(str(val))
                args = ', '.join(args_list)
            else:
                # Handle other cases (single value)
                if isinstance(test_values[j], (int, float)) and test_values[j] < 0:
                    test_values[j] = abs(test_values[j])  # Take absolute value of negative numbers
                
                if isinstance(test_values[j], str):
                    args = repr(test_values[j])  # Use repr for proper string escaping
                elif isinstance(test_values[j], list):
                    processed_list = [abs(v) if isinstance(v, (int, float)) and v < 0 else v for v in test_values[j]]
                    args = repr(processed_list)
                else:
                    args = str(test_values[j])

            function_call = function_names[i] + '(' + args + ')'

            print_statement = 'print("Result ' + str(j + 1) + ': " + str(' + function_call + '))'

            output, errored = local_executor(code_strings[i] + '\n' + print_statement)
            
            input_invocations[-1].append(print_statement)
            output_invocations[-1].append(str(output))
            errored_lst[-1].append(errored)
        
        if any(errored_lst[-1]):
            error_count += 1
        
    print(f"Number of failed test probs: {error_count}")

    return input_invocations, output_invocations, errored_lst


class LLMInference:
    def __init__(self, model_name: str, num_invocations: int):
        self.model_name = model_name
        self.num_invocations = num_invocations
    
        self.base_message = f"I have a Python program. I need you to call the function defined in the program EXACTLY {self.num_invocations} times with different inputs. Call each function in the following format: print('Result i: ' + str(function_name(args))) where each print statement is on a new line. "

        if self.num_invocations == 1:
            self.base_message += "For instance, if the function is 'def add(a, b):\n    return a + b', the output should be 'print('Result 1: ' + str(add(1, 2)))"
        elif self.num_invocations == 2:
            self.base_message += "For instance, if the function is 'def add(a, b):\n    return a + b', the output should be 'print('Result 1: ' + str(add(1, 2)))\nprint('Result 2: ' + str(add(13, 24)))"
        else:
            self.base_message += f"For instance, if the function is 'def add(a, b):\n    return a + b', the output should be 'print('Result 1: ' + str(add(1, 2)))\nprint('Result 2: ' + str(add(13, 24)))\n... print('Result {self.num_invocations}: ' + str(add(78, 0)))"
    
        self.base_message += f"\nDO NOT ADD ANY ADDITIONAL TEXT. JUST THE FUNCTION CALLS.YOU MUST PRINT EXACTLY {self.num_invocations} FUNCTION CALLS EACH ON A NEW LINE.\n\nHere is the Python program to generate the function calls for:\n"
        
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def __call__(self, code_string):

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": self.base_message + code_string
                }
                ]
        )

        return clean_code(completion.choices[0].message.content.strip())



    

def process_code_string(args, max_tries: int = 3):
    index, code_string, model_name, num_invocations = args
    
    local_llm = LLMInference(model_name, num_invocations)
    for i in range(max_tries):
        try:
            model_generated_invocations = local_llm(code_string).split("\n")
            
            model_generated_invocations = process_model_invocations(model_generated_invocations)
            
            assert len(model_generated_invocations) == num_invocations, f"Model generated invocations mismatch: {len(model_generated_invocations)} != {num_invocations}"
            break
        
        except AssertionError:
            if i == max_tries - 1: 
                print(f"Failed to generate correct number of invocations after {max_tries} tries for code at index {index}")
                return index, [], [], []
            else:
                continue

    input_list = []
    output_list = []
    errored_lst = []
    for invocation in model_generated_invocations:
        input_list.append(invocation)

        output, errored = local_executor(code_string + '\n' + invocation)
        output_list.append(output)
        errored_lst.append(errored)

    return index, input_list, output_list, errored_lst

def create_prompt_invocations_llm(num_invocations: int, code_strings: list, function_names: list, model_name: str, max_tries: int = 3):
    tasks = [(i, code_string, model_name, num_invocations) for i, code_string in enumerate(code_strings)]

    input_invocations = [None] * len(code_strings)
    output_invocations = [None] * len(code_strings)
    errored_lst = [None] * len(code_strings)

    num_workers = min(multiprocessing.cpu_count(), len(code_strings))
    
    with tqdm(total=len(code_strings), desc="Creating prompt invocations", colour="green") as pbar:
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            # Submit all tasks
            future_to_index = {executor.submit(functools.partial(process_code_string, max_tries=max_tries), task): task[0] for task in tasks}
            for future in as_completed(future_to_index):
                try:
                    index, inputs, outputs, errored = future.result()
                    input_invocations[index] = inputs
                    output_invocations[index] = outputs
                    errored_lst[index] = errored
                    pbar.update(1)
                except Exception as e:
                    print(f"Error processing code string {future_to_index[future]}: {str(e)}")
                    raise e
                    pbar.update(1)
    
    if None in input_invocations or None in output_invocations:
        raise RuntimeError("Some tasks failed to complete successfully")
        
    return input_invocations, output_invocations, errored_lst



def main(dataset_type: str = "anonymous", num_invocations: int = 10, fnc_creation_strategy: str = "llm", model_name: str = 'gpt-4o', max_tries: int = 3, sft_distillation: bool = False):
    
    if fnc_creation_strategy == "llm":
        assert model_name is not None, "Model name is required for function creation strategy"
    
    code_strings = read_dataset_files(dataset_type, sft_distillation)
    function_names = extract_function_names(code_strings)
    input_invocations, output_invocations, errored_lst = create_prompt_invocations_from_existing_test_cases(num_invocations, code_strings, function_names) if fnc_creation_strategy == "existing_test_cases" else create_prompt_invocations_llm(num_invocations, code_strings, function_names, model_name, max_tries)
    
    if sft_distillation:
        out_dir = Path(f'prompt_invocations/sft/{dataset_type}/num_invocations={num_invocations}/{fnc_creation_strategy}/invocations.json')
    else:
        out_dir = Path(f'prompt_invocations/{dataset_type}/num_invocations={num_invocations}/{fnc_creation_strategy}/invocations.json')
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    
    results = {}
    
    for i, (input_invocations, output_invocations, errored_lst) in enumerate(zip(input_invocations, output_invocations, errored_lst)): 
        results[i] = {}
        for j, (input, output, errored) in enumerate(zip(input_invocations, output_invocations, errored_lst)): 
            results[i][j] = {
                "input": input,
                "output": output,
                "errored": errored
            }

    with open(out_dir, 'w') as f:
        json.dump(results, f)



if __name__ == "__main__":
    fire.Fire(main)






 
    
    
    
