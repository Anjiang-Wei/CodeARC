import re
import os

import pandas as pd
import os
import re
from tqdm import tqdm
from typing import List, Tuple, Dict, Set, Optional, Union, Any
from collections import defaultdict, Counter, deque, OrderedDict
from pathlib import Path
from wrapt_timeout_decorator import timeout
import subprocess
import uuid

def clean_code(response):
    return re.sub(r"^```python\s*|\s*```$", '', response, flags=re.MULTILINE).strip()

def extract_function_names(code_strings: list) -> list:
    """
    Extracts the function name from each code string.
    
    Args:
        code_strings: List of Python code strings, each containing a function definition
    
    Returns:
        List of function names corresponding to each code string.
        If a code string contains both 'main()' and exactly one other function,
        the name of the other function is returned.
    """
    function_names = []
    
    for code in code_strings:
        # Use regex to find only top-level function definitions (with no or minimal indentation)
        # This will match function definitions that start at the beginning of a line with optional whitespace
        # but not heavily indented functions (which are likely nested)
        matches = re.findall(r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code, re.MULTILINE)
        
        if matches:
            # Check if there's a main function 
            if 'main' in matches:
                # Get the other function name (not 'main')
                other_function = [name for name in matches if name != 'main'][-1]
                function_names.append(other_function)
            else:
                # Otherwise, use the last function found since helper functions at the top
                function_names.append(matches[-1])
        else:
            import pdb; pdb.set_trace()
    
    return function_names

def process_model_invocations(model_generated_invocations: list):
    model_generated_invocations = [invocation.strip() for invocation in model_generated_invocations if invocation.strip()]
    model_generated_invocations = [invocation for invocation in model_generated_invocations if invocation.startswith("print(")] 
    return model_generated_invocations

def read_dataset_files(dataset_type: str, sft_distillation: bool = False) -> list:
    """
    Reads all Python files from the specified dataset directory.
    
    Args:
        dataset_type: The subdirectory name under '/home/tarun/SynBench/dataset/'
    
    Returns:
        List of strings containing the content of each Python file, sorted by numeric filename
    """
    # Define the directory path
    directory = f"dataset/{dataset_type}" if not sft_distillation else f"dataset/sft/{dataset_type}"
    
    # Get all Python files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    
    # Define a function to extract numeric value from filename
    def get_numeric_value(filename):
        # Extract numeric part before .py extension
        match = re.match(r'(\d+)\.py', filename)
        if match:
            return int(match.group(1))
        return float('inf')  # Non-matching files will be sorted to the end
    
    # Sort files by numeric value
    files.sort(key=get_numeric_value)
    
    # Read content of each file into a list of strings
    code_strings = []
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as f:
            code_strings.append(f.read())
    
    return code_strings
def local_executor(code_string, timeout=5):
    """
    Execute the provided code string in a local namespace with common libraries available.
    Captures and returns the stdout output from the execution.
    
    Args:
        code_string: The Python code to execute
        timeout: Maximum execution time in seconds (default: 5)
        
    Returns:
        The stdout output from the code execution, or None if an error occurred
    """    
    # Generate a unique identifier for this execution
    unique_id = str(uuid.uuid4())
    
    # Create a directory if it doesn't exist
    output_dir = Path("output/temp/executor")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a file path with the unique ID
    temp_file_path = output_dir / f"code_{unique_id}.py"

    # Write the code to the file
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write(code_string)
    
    try:
        # Run the code in a separate process with timeout
        process = subprocess.run(
            ['python3', str(temp_file_path)],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        # Get the output
        output = process.stdout.strip()
        
        # Check if there was an error
        if process.returncode != 0:
            return process.stderr.strip(), True
        
        # Clean up the file after execution
        try:
            os.remove(temp_file_path)
        except:
            pass  # Ignore cleanup errors
            
        return output, False
    
    except subprocess.TimeoutExpired:
        # Clean up the file after timeout
        try:
            os.remove(temp_file_path)
        except:
            pass  # Ignore cleanup errors
        return f'Execution timed out after {timeout} seconds', True
    
    except Exception as e:
        # Clean up the file after exception
        try:
            os.remove(temp_file_path)
        except:
            pass  # Ignore cleanup errors
        return str(e), True


# if __name__ == "__main__":
#     code_str = 'def solution(nums: list[int]) -> list[int]:\n    """\n    Extracts numbers at even indices from the list and returns their squares.\n    Example: [1, 2, 3, 4, 5] -> [1, 9, 25]\n    """\n    result = []\n    for i in range(0, len(nums), 2):\n        result.append(nums[i] ** 2)\n    return result\n\nprint(\'Result 12: \' + str(solution([10, 20])))'
#     print(local_executor(code_str))
