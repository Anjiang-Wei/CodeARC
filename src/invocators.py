from abc import ABC, abstractmethod
from utils import local_executor, clean_code, process_model_invocations, extract_function_names
from openai import OpenAI
import os
from typing import List, Tuple, Dict
import yaml
from copy import deepcopy
from tqdm import tqdm
import asyncio
from pathlib import Path
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from differential_testing.diff_testing import test
from llm_generate import llm_generate, EvalInput


def generate(eval_strategy: str, model_name: str, problem_id: int,  version_id: int, anonymous: bool, synthesized_code: str):
    correct_file = "dataset/" + ("anonymous" if anonymous else "annotated") + f"/{problem_id}.py"
    correct_executable = open(correct_file, "r").read()
    
    # create directory
    path = f"output/temp/examples/{eval_strategy}/{model_name}/P{problem_id}_V{version_id}_{anonymous}"
    Path(path).mkdir(parents=True, exist_ok=True)

    # write correct program to correct.py
    with open(f"{path}/correct.py", "w") as f:
        f.write(correct_executable)

    # write synthesized program to incorrect.py
    with open(f"{path}/incorrect.py", "w") as f:
        f.write(synthesized_code)
    # print(f"Problem {problem_id}, Version {version_id}, Anonymous {anonymous} done.")

async def diff_tester(eval_strategy, model_name, problem_id, version_id, anonymous, synthesized_code):
    generate(eval_strategy, model_name, problem_id, version_id, anonymous, synthesized_code)
    correctness_result = await test(eval_strategy, model_name, problem_id, version_id, anonymous) 
    # both return null, return False
    if correctness_result['pynguin']['Equivalent'] not in (True, False) and correctness_result['mokav']['Equivalent'] not in (True, False):
        return False, "Failed for some input"
    # only pynguin returns null, then trust mokav's True
    if correctness_result['pynguin']['Equivalent'] not in (True, False) and correctness_result['mokav']['Equivalent'] in (True, False):
        if correctness_result['mokav']['Equivalent'] == True:
            return True, None
    # only mokav returns null, then trust pynguin's True
    if correctness_result['mokav']['Equivalent'] not in (True, False) and correctness_result['pynguin']['Equivalent'] in (True, False):
        if correctness_result['pynguin']['Equivalent'] == True:
            return True, None
    
    is_correct = correctness_result['pynguin']['Equivalent'] and correctness_result['mokav']['Equivalent']
    
    if not is_correct:
        diff_inputs_dict_lst = correctness_result['mokav']['differing_inputs']
        if len(diff_inputs_dict_lst) >= 1: 
            diff_inputs_dict = diff_inputs_dict_lst[0]
            failed_input = diff_inputs_dict['input']
            failed_expected_output = diff_inputs_dict['values'].split('\\n\\n')[0]
            error_message = f"Failed input: {failed_input}\nGround Truth != Output From Generated Code: {failed_expected_output}"
        else:
            error_message = "Failed for some input"
    else:
        error_message = None
    
    return is_correct, error_message



class BaseInvocator(ABC):
    def __init__(self, model_name: str, prompt_path: str, max_invocations: int = 100, max_tries: int = 3, anonymous: bool = False):
        self.model_name = model_name
        # self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.max_invocations = max_invocations
        self.max_tries = max_tries
        self.anonymous = anonymous

        with open(prompt_path, 'r') as f:
            self.prompt_config = yaml.safe_load(f)
    
    @abstractmethod
    async def __call__(self, input_invocations: List[str], output_invocations: List[str], prob_idx: int, gt_function: str) -> Tuple[bool, Dict]:
        pass
    
    def convo_history_as_string(self, messages: list) -> list: 
        convo_history = ''
        for message in messages:
            convo_history += f"{message['role'].upper()}:\n{message['content']}\n\n"
        
        return [{'role': 'user', 'content': convo_history}]
    
    async def generate_code_completion(self, messages: list) -> str:
        input = EvalInput(messages=messages, model_with_platform=self.model_name)
        return await llm_generate(input)
        

class ReasoningGuidedInvocator(BaseInvocator):
    def __init__(self, model_name: str, prompt_path: str, max_invocations: int = 100, max_debug_rounds: int = 3, max_tries: int = 3, anonymous: bool = False):
        super().__init__(model_name, prompt_path, max_invocations, max_tries, anonymous)
        self.max_debug_rounds = max_debug_rounds
        self.eval_strategy = f'reasoning_guided_mi={max_invocations}_mdr={max_debug_rounds}'
    
    async def __call__(self, input_invocations: List[str], output_invocations: List[str], prob_idx: int, gt_function: str) -> Tuple[bool, Dict]:
        fnc_name = extract_function_names([gt_function])[0]
        results_trace = {}
        
        is_correct = False
        
        num_debugs_left = self.max_debug_rounds
        num_invocations_left = self.max_invocations - len(input_invocations)
        
        i = 0
        last_action = None
        synthesized_id = 0
        messages = []
        

        with tqdm(desc=f"Processing Problem prob_idx={prob_idx}, anonymous={self.anonymous}", colour="blue") as pbar:
            while num_debugs_left > 0 or num_invocations_left > 0:
                if i == 0:
                    if num_invocations_left == 0: 
                        prompt = self.prompt_config['reasoning_guided']['base_no_invocations'].replace('[FUNCTION_NAME]', fnc_name).replace('[INPUT_INVOCATIONS]', '\n'.join(input_invocations)).replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_invocations)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left))
                    elif num_debugs_left == 0: 
                        prompt = self.prompt_config['reasoning_guided']['base_no_debugging'].replace('[FUNCTION_NAME]', fnc_name).replace('[INPUT_INVOCATIONS]', '\n'.join(input_invocations)).replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_invocations)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left))
                    else: 
                        prompt = self.prompt_config['reasoning_guided']['base'].replace('[FUNCTION_NAME]', fnc_name).replace('[INPUT_INVOCATIONS]', '\n'.join(input_invocations)).replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_invocations)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left))
                else:
                    if last_action == 'IMPLEMENTATION':
                        if num_invocations_left == 0: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_draft_implementation_previous_iteration_no_invocations'].replace('[FAILED_INPUTS]', failed_inputs).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                        elif num_debugs_left == 0: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_draft_implementation_previous_iteration_no_debugging'].replace('[FAILED_INPUTS]', failed_inputs).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                        else: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_draft_implementation_previous_iteration'].replace('[FAILED_INPUTS]', failed_inputs).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                    else:
                        if num_invocations_left == 0: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_invocations_previous_iteration_no_invocations'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                        elif num_debugs_left == 0: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_invocations_previous_iteration_no_debugging'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                        else: 
                            prompt = self.prompt_config['reasoning_guided']['iteration']['generated_invocations_previous_iteration'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)

                
                messages.append({'role': 'user', 'content': prompt})
                success =  False
                for j in range(self.max_tries):
                    model_raw_output = await self.generate_code_completion(messages) # TODO: error_handlling
                    if type(model_raw_output) == str:
                        model_raw_output = model_raw_output.strip()
                    else:
                        model_raw_output = ""
                    
                    if 'IMPLEMENTATION' in model_raw_output:
                        program = clean_code(model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')])
                        if program == "":
                            is_correct, failed_inputs = False, "ALL INPUTS"
                        else:
                            is_correct, failed_inputs = await diff_tester(self.eval_strategy, self.model_name, prob_idx, synthesized_id, self.anonymous, program)
                        synthesized_id += 1
                        last_action = 'IMPLEMENTATION'
                        results_trace[i] = {'is_correct': is_correct, 'failed_inputs': failed_inputs, 'program': program, 'action': last_action, 'model_response': model_raw_output}
                        messages.append({'role': 'assistant', 'content': model_raw_output})
                        if num_debugs_left == 0 or is_correct: 
                            return (is_correct, results_trace, messages)
                        
                        num_debugs_left -= 1
                        pbar.set_postfix({"action": "IMPLEMENTATION", "debugs_left": num_debugs_left})
                        success = True
                        break
                    
                    elif 'INVOCATIONS' in model_raw_output and num_invocations_left > 0:
                        invocations_block = model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')]
                        new_invocations = process_model_invocations(clean_code(invocations_block).split('\n'))
                        
                        if len(new_invocations) > num_invocations_left:
                            continue
                        
                        messages.append({'role': 'assistant', 'content': model_raw_output})
                        output_list = []
            
                        for invocation in new_invocations: 
                            output, _ = local_executor(gt_function + '\n' + invocation)
                            output_list.append(output)
                    
                        last_action = 'INVOCATIONS'
                        results_trace[i] = {'action': last_action, 'generated_invocations': new_invocations, 'invocations_outputs': output_list, 'model_response': model_raw_output}
                        
                        num_invocations_left -= len(new_invocations)
                        pbar.set_postfix({"action": "INVOCATIONS", "invocations_left": num_invocations_left})
                        success = True
                        break
                        
                if not success:
                    results_trace[i] = {'action': "INVALID_ACTION", 'model_response': model_raw_output}
                    return (is_correct, results_trace, messages)
                
                i += 1
                pbar.update(1)
                
                if num_debugs_left < 0 or num_invocations_left < 0:
                    raise RuntimeError("Invalid state: this should never happen")
        
        # Final implementation attempt
        if last_action == 'IMPLEMENTATION': 
            prompt = self.prompt_config['reasoning_guided']['final']['generated_draft_implementation_previous_iteration'].replace('[FAILED_INPUTS]', failed_inputs).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
        elif last_action == 'INVOCATIONS':
            prompt = self.prompt_config['reasoning_guided']['final']['generated_invocations_previous_iteration'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
        else:
            if self.max_debug_rounds == 0 and self.max_invocations - len(input_invocations) == 0:
                prompt = self.prompt_config['reasoning_guided']['final']['generated_invocations_previous_iteration'].replace('[OUTPUT_INVOCATIONS]', '').replace('[MAX_INVOCATIONS]', '0').replace('[MAX_CHECKS]', '0').replace('[FUNCTION_NAME]', fnc_name)
                prompt += "\n\n Despite what is previously discussed, in this current setting, you will not have information about 'OUTPUT_INVOCATIONS' or 'FAILED_INPUTS'. You must directly generate the Python implementation given the initial input-output pairs with no additional information."
            else:
                raise RuntimeError("Invalid last action: this should never happen")
        
        messages.append({'role': 'user', 'content': prompt})
        
        model_raw_output = await self.generate_code_completion(messages) # TODO: error_handlling 
        program = clean_code(model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')])
        if program == "":
            is_correct, failed_inputs = False, "ALL INPUTS"
        else:
            is_correct, failed_inputs = await diff_tester(self.eval_strategy, self.model_name, prob_idx, synthesized_id, self.anonymous, program) 
        results_trace[i+1] = {'is_correct': is_correct, 'failed_inputs': failed_inputs, 'program': program, 'action': 'IMPLEMENTATION', 'model_response': model_raw_output}
        messages.append({'role': 'assistant', 'content': model_raw_output})
        return (is_correct, results_trace, messages)        

class SFTDistillation(ReasoningGuidedInvocator):
    def __init__(self, model_name: str, prompt_path: str, max_invocations: int = 100, max_debug_rounds: int = 3, max_tries: int = 3, anonymous: bool = False):
        super().__init__(model_name, prompt_path, max_invocations, max_debug_rounds, max_tries, anonymous)
        self.eval_strategy = f'sft_distillation_mi={max_invocations}_mdr={max_debug_rounds}'

    async def __call__(self, input_invocations: List[str], output_invocations: List[str], prob_idx: int, gt_function: str) -> Tuple[bool, Dict]:
        fnc_name = extract_function_names([gt_function])[0]
        results_trace = {}
        
        is_correct = False
        
        num_debugs_left = self.max_debug_rounds
        num_invocations_left = self.max_invocations - len(input_invocations)
        
        i = 0
        synthesized_id = 0
        messages = []
        

        with tqdm(desc=f"Processing Problem {prob_idx}", colour="blue") as pbar:
            while num_debugs_left > 0 or num_invocations_left > 0:
                if i == 0:
                    prompt = self.prompt_config['reasoning_guided']['base'].replace('[FUNCTION_NAME]', fnc_name).replace('[INPUT_INVOCATIONS]', '\n'.join(input_invocations)).replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_invocations)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left))
                    prompt = self.prompt_config['sft_distillation']['base'].replace('[FUNCTION_NAME]', fnc_name).replace('[FUNCTION_BODY]', gt_function) + '\n' + prompt
                else:
                    prompt = self.prompt_config['reasoning_guided']['iteration']['generated_invocations_previous_iteration'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
                    prompt = self.prompt_config['sft_distillation']['iteration']['generated_invocations_previous_iteration'].replace('[FUNCTION_BODY]', gt_function) + '\n' + prompt
                
                messages.append({'role': 'user', 'content': prompt})
                success =  False
                for j in range(self.max_tries):
                    model_raw_output = await self.generate_code_completion(messages) # TODO: error_handlling
                    if type(model_raw_output) == str:
                        model_raw_output = model_raw_output.strip()
                    else:
                        model_raw_output = ""
                    
                    if 'IMPLEMENTATION' in model_raw_output:
                        program = clean_code(model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')])
                        is_correct, failed_inputs = True, None
                        synthesized_id += 1
                        last_action = 'IMPLEMENTATION'
                        results_trace[i] = {'is_correct': is_correct, 'failed_inputs': failed_inputs, 'program': program, 'action': last_action, 'model_response': model_raw_output}
                        messages.append({'role': 'assistant', 'content': model_raw_output})
                        return (is_correct, results_trace, messages)
             
                    elif 'INVOCATIONS' in model_raw_output and num_invocations_left > 0:
                        invocations_block = model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')]
                        new_invocations = process_model_invocations(clean_code(invocations_block).split('\n'))
                        
                        if len(new_invocations) > num_invocations_left:
                            continue
                        
                        messages.append({'role': 'assistant', 'content': model_raw_output})
                        output_list = []
            
                        for invocation in new_invocations: 
                            output, _ = local_executor(gt_function + '\n' + invocation)
                            output_list.append(output)
                    
                        last_action = 'INVOCATIONS'
                        results_trace[i] = {'action': last_action, 'generated_invocations': new_invocations, 'invocations_outputs': output_list, 'model_response': model_raw_output}
                        
                        num_invocations_left -= len(new_invocations)
                        pbar.set_postfix({"action": "INVOCATIONS", "invocations_left": num_invocations_left})
                        success = True
                        break
                        
                if not success:
                    results_trace[i] = {'action': "INVALID_ACTION", 'model_response': model_raw_output}
                    return (is_correct, results_trace, messages)
                
                i += 1
                pbar.update(1)
                
                if num_debugs_left < 0 or num_invocations_left < 0:
                    raise RuntimeError("Invalid state: this should never happen")
        

        prompt = self.prompt_config['reasoning_guided']['final']['generated_invocations_previous_iteration'].replace('[OUTPUT_INVOCATIONS]', '\n'.join(output_list)).replace('[MAX_INVOCATIONS]', str(num_invocations_left)).replace('[MAX_CHECKS]', str(num_debugs_left)).replace('[FUNCTION_NAME]', fnc_name)
        prompt = self.prompt_config['sft_distillation']['final']['generated_invocations_previous_iteration'].replace('[FUNCTION_BODY]', gt_function) + '\n' + prompt
        messages.append({'role': 'user', 'content': prompt})
        
        model_raw_output = await self.generate_code_completion(messages) # TODO: error_handlling
        program = clean_code(model_raw_output[model_raw_output.rfind('```python'):model_raw_output.rfind('```')])
        is_correct, failed_inputs = True, None 
        results_trace[i+1] = {'is_correct': is_correct, 'failed_inputs': failed_inputs, 'program': program, 'action': 'IMPLEMENTATION', 'model_response': model_raw_output}
        messages.append({'role': 'assistant', 'content': model_raw_output})
        return (is_correct, results_trace, messages)  
