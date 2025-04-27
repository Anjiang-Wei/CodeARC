#!/usr/bin/env python3
import os
import re
import sys
import glob
from pathlib import Path

def find_function_and_rename(file_path):
    """
    Find the first executable function in a Python file and rename it to 'solution'
    Returns True if successful, False otherwise
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Regular expression to find a function definition
    pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    
    matches = re.findall(pattern, content)
    
    if not matches:
        print(f"Warning: No function found in {file_path}")
        return False
    
    # Get the first function name (assuming it's the main executable function)
    old_function_name = matches[0]
    
    # Skip if the function is already named 'solution'
    if old_function_name == 'solution':
        print(f"Function in {file_path} is already named 'solution'")
        return True
    
    print(f"Renaming function '{old_function_name}' to 'solution' in {file_path}")
    
    # Replace the function name with 'solution'
    new_content = re.sub(
        r'def\s+' + re.escape(old_function_name) + r'\s*\(', 
        'def solution(', 
        content
    )
    
    # Also replace any recursive call
    new_content = re.sub(
        r'\b' + re.escape(old_function_name) + r'\s*\(', 
        'solution(', 
        new_content
    )
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # differential_testing directory
    parent_dir = os.path.dirname(script_dir)
    examples_dir = os.path.join(parent_dir, "output", "temp", "examples")
    
    if not os.path.exists(examples_dir):
        print(f"Error: Examples directory not found at {examples_dir}")
        return
    
    # Get all example directories 
    example_dirs = [d for d in os.listdir(examples_dir) if os.path.isdir(os.path.join(examples_dir, d)) and d.startswith("example")]
    
    for example_dir_name in example_dirs:
        example_dir_path = os.path.join(examples_dir, example_dir_name)
        
        # Process correct.py
        correct_file = os.path.join(example_dir_path, "correct.py")
        if os.path.exists(correct_file):
            find_function_and_rename(correct_file)
        
        # Process incorrect.py
        incorrect_file = os.path.join(example_dir_path, "incorrect.py")
        if os.path.exists(incorrect_file):
            find_function_and_rename(incorrect_file)
    
    print("Function renaming complete!")

if __name__ == "__main__":
    main()