from .test_generator import TestGenerator
from .utils import write_to_file, run_process, read_file
import ast
import logging
import os
import json
import asyncio
import shutil
from pathlib import Path

class CodeRunner:
    def __init__(self, is_func, is_qb, iteration_count, meta_data_config, generated_tests_dir, number_of_samples, temperature, problem_dir_hash) -> None:
        self.is_func = is_func
        self.is_qb = is_qb
        self.iteration_count = iteration_count
        self.test_generator = TestGenerator(config=meta_data_config, number_of_samples=number_of_samples, temperature=temperature, is_qb=is_qb, problem_dir_hash=problem_dir_hash)
        self.generated_tests_dir = generated_tests_dir
        self.number_of_samples = number_of_samples
        self.temperature = temperature
        self.contain_exec_diff = 'E' in meta_data_config
        self.problem_dir_hash = problem_dir_hash
        Path("output/temp/mokav").mkdir(parents=True, exist_ok=True)

    def extract_function_name(self, code):
        return code.split("def ")[1].split("(")[0]
    
    def is_multi_argument(self, acc_code):
        """
        Determines if the function in acc_code has multiple arguments.
        
        Args:
            acc_code (str): The function code to analyze
            
        Returns:
            bool: True if the function has more than one argument, False otherwise
        """
        try:
            # Parse the code into an AST
            tree = ast.parse(acc_code)
            
            # Find the function definition node
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Count the arguments
                    arg_count = len(node.args.args)
                    
                    # Return True if there are multiple arguments
                    return arg_count > 1
                    
            # If no function definition found or only one argument
            return False
        except Exception as e:
            logging.error(f"Error analyzing function arguments: {str(e)}")
            return False

    def create_unnitest(self, buggy_code, acc_code, test_cases, author_id=None, problem_id=None):
        with open(f"output/temp/mokav/temp_acc_qb_{self.problem_dir_hash}.py", "w") as f:
            f.write(acc_code)
        
        acc_func_name = self.extract_function_name(acc_code)

        is_input_multi_arg = self.is_multi_argument(acc_code)

        with open(f"output/temp/mokav/temp_bug_qb_{self.problem_dir_hash}.py", "w") as f:
            f.write(buggy_code)

        bug_func_name = self.extract_function_name(buggy_code)

        unittest_str = f"""
import unittest
from temp_acc_qb_{self.problem_dir_hash} import {acc_func_name} as patched_source
from temp_bug_qb_{self.problem_dir_hash} import {bug_func_name} as original_source

class TestFunctions(unittest.TestCase):
                
"""

        for i, test_case in enumerate(test_cases):
            input_data = test_case["inputdata"]

            # print input
            # print(f"input_data: {input_data}")

            is_input_list = False

            if "\n" in str(input_data):
                input_data = list(str(input_data).split("\n"))
                is_input_list = True

            is_input_list = is_input_list or type(input_data) is tuple

            # if it's floating point, then it should not be a string!
            # if not is_input_list:
            #     input_data = f'"{input_data}"'

            if type(input_data) is str:
                input_data = f'"{input_data}"'

            unittest_str = (
                unittest_str
                + f"""

    def test{i}(self):
        input_{i} = {input_data}
        out1 = None
        out2 = None
        error1 = 'No Error'
        error2 = 'No Error'
        
        try:
            out1 = patched_source({"*" if is_input_multi_arg else ""}input_{i})
        except Exception:
            error1 = 'Error'
            
        try:
            out2 = original_source({"*" if is_input_multi_arg else ""}input_{i})
        except Exception:
            error2 = 'Error'
            
        self.assertEqual(error1, error2)
        
        if error1 == 'No Error' and error2 == 'No Error':
            self.assertEqual(out1, out2)
            
"""
            )

        unittest_str += """
if __name__ == '__main__':
    unittest.main()  
    
    """

        with open(f"output/temp/mokav/temp_test_case_{self.problem_dir_hash}.py", "w") as f:
            f.write(unittest_str)
   
    def change_test_to_dict(self, test_case) -> list:
        data_list = []
        for difference_exposing_test in test_case:
            if difference_exposing_test:
                try:
                    data_list.append(ast.literal_eval(
                        difference_exposing_test[0].replace("python", "")))
                except Exception as e:
                    print(e)
                    logging.info(f"ast.literal_eval error: {e}")
                    continue
        return data_list

    def process_input_data(self, input_data):
        if "\n" in str(input_data):
            return list(str(input_data).split("\n"))
        return input_data

    async def generate_test_and_run_until_assertion_error(self, rej, acc1, existing_test, existing_test_output, 
                                                    output_code, author_id, problem_id, is_iteration=False):

        acc_unique_var_state, rej_unique_var_state = None, None

        try:
            if self.contain_exec_diff:
                acc_unique_var_state, rej_unique_var_state = self.get_exec_diff(existing_test["inputdata"], acc1, rej)
        except Exception as e:
            logging.info(f"###EXCEPTION###: {e}")

        test_case = await self.test_generator.generate_test(
            rej, acc1, existing_test, existing_test_output, output_code, author_id=author_id, 
            problem_id=problem_id, acc_unique_var_state=acc_unique_var_state, bug_unique_var_state=rej_unique_var_state, is_iteration=is_iteration) # TODO: Error Handling
        data_list = self.change_test_to_dict(test_case)

        #print data list
        # print(f"data_list: {data_list}")

        # Save directory for the test cases
        base_save_dir = getattr(self, 'example_save_dir', None)
        
        # Convert is_iteration to an iteration number
        iteration_number = is_iteration if isinstance(is_iteration, int) else 0
        
        # Create iteration-specific directory if we have a base save directory
        if base_save_dir:
            iteration_dir = os.path.join(base_save_dir, f"iteration_{iteration_number}")
            os.makedirs(iteration_dir, exist_ok=True)
            
            # Save copies for test dirs - using shutil.copy instead of os.system
            shutil.copy(f'output/temp/mokav/temp_acc_qb_{self.problem_dir_hash}.py', f'{iteration_dir}/temp_acc_qb.py')
            shutil.copy(f'output/temp/mokav/temp_bug_qb_{self.problem_dir_hash}.py', f'{iteration_dir}/temp_bug_qb.py')
        else:
            iteration_dir = None
        
        # Create unittests with single test method
        test_output = ''
        found_assertion_error = False
        
        for i, data in enumerate(data_list):
            try:
                self.create_unnitest(rej, acc1, [data])
                output = str(
                    run_process(["python", f"output/temp/mokav/temp_test_case_{self.problem_dir_hash}.py"], timeout=2)
                )
                test_output += '\n NEW TEST OUTPUT: \n' + output
                
                # Save each individual test case if we have a save directory
                if iteration_dir:
                    # Save this specific test case
                    Path(iteration_dir).mkdir(parents=True, exist_ok=True)
                    with open(f"{iteration_dir}/test_case_{i}.py", "w") as f:
                        with open(f"output/temp/mokav/temp_test_case_{self.problem_dir_hash}.py", "r") as temp:
                            f.write(temp.read())
                
                if ("AssertionError" in output):
                    logging.info(f"###IS_DET###: {author_id},{output}")
                    found_assertion_error = True
                else:
                    logging.info(f"###IS_NOT_DET###: {author_id},{output}")
            except Exception as e:
                test_output += f"\n NEW TEST OUTPUT: \nException: {e}"

        # Save the combined output for this iteration
        if iteration_dir:
            with open(f"{iteration_dir}/all_tests_output.txt", "w") as f:
                f.write(test_output)

        return test_output, data_list

    def get_code_output(self, input_data, code, is_acc=True, collect_var_states=False):
        module_name = 'acc' if is_acc else 'bug'
        # Modified to use 'solution' as the function name
        old_function_name = self.extract_function_name(code)
        func_name = 'solution'

        if "\n" in str(input_data):
            input_data = list(input_data.split("\n"))

        is_input_list = type(input_data) is list or type(input_data) is tuple

        if not is_input_list:
            input_data = f'"{input_data}"'
        
        with open(f"output/temp/mokav/temp_{module_name}_qb_{self.problem_dir_hash}.py", "w") as f:
            f.write(code)

        filename = f"output/temp/mokav/temp_{module_name}_exec_{self.problem_dir_hash}.py"
        with open(filename, "w") as f:
            f.write(f'''
from temp_{module_name}_qb_{self.problem_dir_hash} import {old_function_name} as {func_name}
input_data = {input_data}
output_code = {func_name}({"*" if is_input_list else ""}input_data)
#output_code = list(output_code)
print(output_code)
''')

        if collect_var_states:
            process_acc_exec = run_process(["python", "-m", "spotflow", "-t", f"{func_name}", "unittest", filename], 2)
        else:
            process_acc_exec = run_process(["python", filename], 2)

        if type(process_acc_exec) is str:
            return process_acc_exec
        else:
            output = str(process_acc_exec.stdout.decode()).strip()
            return output
    
    def get_var_states(self, input_data, code, is_acc=True):
        var_info = {}

        output = self.get_code_output(input_data, code, is_acc=is_acc, collect_var_states=True)
        lines = output.splitlines()
        
        is_var_state = False
        for i, l in enumerate(lines):
            if 'VarStateHistory' in l:
                is_var_state = True
                continue

            if not is_var_state:
                continue

            if 'ReturnState:' in l:
                break


            l = l.removeprefix('- ') 
            var_name, var_values = (l.split(': ')[0], ': '.join(l.split(': ')[1:]))

            if var_name == 'args' or var_name == 'global_list':
                continue

            var_values = [x for x in var_values.split(' #SPLITTER# ') if len(str(x)) < 50]
            var_info[var_name] = {'states': set(var_values), 'ind': i}

        return var_info

    def get_first_unique_state(self, l_var_info, r_var_info):
        common_vars = list(set(l_var_info.keys()).intersection(set(r_var_info.keys())))

        common_vars.sort(key=lambda var: l_var_info[var]['ind'])

        for var in common_vars:
            l_states = l_var_info[var]['states']
            r_states = r_var_info[var]['states']

            unique_states = l_states.difference(r_states)

            if len(unique_states) > 0:
                return (var, list(unique_states)[0])

    def get_exec_diff(self, input_data, acc_code, rej_code):
        acc_var_info = self.get_var_states(input_data, acc_code, is_acc=True)
        rej_var_info = self.get_var_states(input_data, rej_code, is_acc=False)

        unique_acc_var_state = self.get_first_unique_state(acc_var_info, rej_var_info)
        unique_rej_var_state = self.get_first_unique_state(rej_var_info, acc_var_info)

        return unique_acc_var_state, unique_rej_var_state

    async def check_test(self, acc1, rej, existing_test, problem_id, author_id):
        try:
            logging.info(f"###(PROBLEM_ID, AUTHOR)###: ({problem_id}, {author_id})")
            existing_test_output = self.get_code_output(existing_test["inputdata"], acc1)

            output, data_list = await self.generate_test_and_run_until_assertion_error(
                rej, acc1, existing_test, existing_test_output, None, author_id, problem_id, is_iteration=0)
            logging.info(f"###ITERATION###: 0")
            logging.info(f"###TEMP_TEST_PY_OUTPUT: \n\n{output}")
            
            result = {
                "Tool": "Mokav"
            }
            
            # Initialize test count with the first run
            total_test_count = len(data_list)
            result["total_tests"] = total_test_count
            
            # Check if the first iteration found a difference
            if "AssertionError" in output:
                result["Equivalent"] = False
                return result
                
            # Continue with additional iterations if needed
            for i in range(self.iteration_count):
                if len(data_list) > 0:
                    input_data = self.process_input_data(data_list[0]["inputdata"])
                    output_code = self.get_code_output(input_data, acc1)
                else:
                    output_code = None

                output, data_list = await self.generate_test_and_run_until_assertion_error(
                    rej, acc1, existing_test, existing_test_output, output_code, author_id, problem_id, is_iteration=i+1)
                logging.info(f"###ITERATION###: {i + 1}")
                logging.info(f"###TEMP_TEST_PY_OUTPUT_RETRY: \n\n{output}")
                
                # Add the tests from this iteration to the total count
                total_test_count += len(data_list)
                result["total_tests"] = total_test_count
                
                if "AssertionError" in output:
                    result["Equivalent"] = False
                    return result
            
            # If we get here, no differences were found
            result["Equivalent"] = True
            return result
            
        except Exception as e:
            logging.info(f"###EXCEPTION###: {e}")
            return {"Tool": "Mokav", "Equivalent": None, "Error": str(e)}
