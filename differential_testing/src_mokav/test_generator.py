from pathlib import Path
from .chatgpt import ChatGPT_2
import re
import logging
import asyncio


class TestGenerator:
    def __init__(self, config, number_of_samples, temperature, is_qb, problem_dir_hash):
        self.config = config
        self.chatgpt = ChatGPT_2(
            default_instruction="As a software testing expert, your task involves generating a test input that can distinguish between two versions of a program. These are versions 'original' and 'patched'.",
            cache_file_path=f"output/temp/ChatGPT_2/cache_{problem_dir_hash}.json",
            default_temp=temperature,
            default_n=number_of_samples
        )
        self.number_of_samples = number_of_samples
        self.temperature = temperature
        self.test_format = "{'inputdata': <inputdata>}"
        self.is_qb = is_qb
        self.prompt_history = []

    def extract_code_blocks(self, text):
        code_blocks = re.findall(r"```(.*?)```", text, re.DOTALL)
        return [block.strip() for block in code_blocks]

    def extract_regex(self, string):
        pattern = r"\{'inputdata': '[^']*'\}"
        matches = re.findall(pattern, string)
        return [block.strip() for block in matches]
    
    def extract_regex_qb(self, string):
        string = string.replace("python", "")
        string = string.strip("`") 
        return [string]

    async def code_description(self, accepted_code):
        description_prompt = f"What is the intention of this code?  {accepted_code}"
        chatgpt_resp = await self.chatgpt.get_response(
            new_question=description_prompt, 
            temp=0, 
            n=1, 
            instruction="You are an intelligent software bot that describes python code. You are given a python code snippet."
        )
        return chatgpt_resp

    def extract_code(self, text):
        pattern = r"```python(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return "".join([match.strip() for match in matches])

    async def generate_test(self, buggy_code, accepted_code, existing_test=None, existing_test_accepted_output=None, 
                      retry_ouput=None, author_id=None, problem_id=None, acc_unique_var_state=None, bug_unique_var_state=None, is_iteration=False):
        responses = []
        if is_iteration:
            prompt = ""
            if "E" in self.config:
                if bug_unique_var_state is not None:
                    prompt += f"""When the your generated test input is executed on version 'original', the variable '{bug_unique_var_state[0]}' is assigned the value '{bug_unique_var_state[1]}'. However, this variable never attains this value in version 'patched'."""
                    if acc_unique_var_state is not None:
                        prompt += f"""
Similarly, during the execution of your generated test input on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}', a value it never attains in version 'original'."""
                elif acc_unique_var_state is not None:
                    prompt += f"""When your generated test input is executed on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}'. However, this variable never attains this value in version 'original'."""
                prompt += f"""
Both versions produce an identical output for your generated test input.""" + f""" This identical output is {retry_ouput}.""" if retry_ouput is not None else ""
            else:
                prompt = "Both versions produce an identical output for your generated test input."
            prompt += " The output should be different. Please generate another test input."
            chatgpt_resp = await self.chatgpt.get_response(
                new_question=prompt, previous_questions_and_answers=self.prompt_history, author_id=author_id, problem_id=problem_id
            )
            
            for i in range(len(chatgpt_resp)):
                responses.append(chatgpt_resp[i])
            self.prompt_history.append((prompt, responses[0]))
        else:
            self.prompt_history = [] # it's an initial prompt

            if "AA" in self.config:
                prompt = f"""
The following code represents version 'patched' of the program: 
```python
{accepted_code}```
"""

                if 'D' in self.config:
                    acc_description = await self.code_description(accepted_code)

                    prompt += f"""
Description of version 'patched': {acc_description}
"""

                prompt += f"""
We also have an 'original' version of this program, which is slightly different from the patched version.
"""
                
                if "I" in self.config:
                    prompt += f"""
Here is a sample test input for which both versions produce identical output:
```python
{existing_test}
```
"""
                    if "E" in self.config:
                        if bug_unique_var_state is not None:
                            prompt += f"""When the above test input is executed on version 'original', the variable '{bug_unique_var_state[0]}' is assigned the value '{bug_unique_var_state[1]}'. However, this variable never attains this value in version 'patched'."""
                            if acc_unique_var_state is not None:
                                prompt += f"""
Similarly, during the execution of the same test input on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}', a value it never attains in version 'original'."""
                        elif acc_unique_var_state is not None:
                            prompt += f"""When the above test input is executed on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}'. However, this variable never attains this value in version 'original'."""

                        prompt += f"""The identical output for this sample test input is: {existing_test_accepted_output}
"""
                prompt += f"""
Your task is to generate a new test input in Python dict format as follows:
```python
{self.test_format}
```
This test input should be designed such that it exposes the differences between the two versions 'original' and 'patched'. In other words, when the test input is given to versions 'original' and 'patched', they should produce different outputs. This can be represented as:
```python
original(inputdata) != patched(inputdata)
```
Please note that your output should not contain any explanation or newline ('\\n') characters. Create a 'difference exposing test' input as per the Python dict format above.
"""
            elif "BA" in self.config:

                prompt = f"""
The following code represents version 'original' of the program:
```python
{buggy_code}
```
"""
                if 'D' in self.config:
                    buggy_description = await self.code_description(buggy_code)

                    prompt += f"""
Description of version 'original': {buggy_description}
"""
                
                prompt += f"""
The following code represents version 'patched' of the same program: 
```python
{accepted_code}
```
"""
                
                if 'D' in self.config:
                    acc_description = await self.code_description(accepted_code)

                    prompt += f"""
Description of version 'patched': {acc_description}
"""
                
                if "I" in self.config:                
                    prompt += f"""
Here is a sample test input for which both versions produce identical output:
```python
{existing_test}
```
"""
                    if "E" in self.config:
                        if bug_unique_var_state is not None:
                            prompt += f""" When the above test input is executed on version 'original', the variable '{bug_unique_var_state[0]}' is assigned the value '{bug_unique_var_state[1]}'. However, this variable never attains this value in version 'patched'."""
                            if acc_unique_var_state is not None:
                                prompt += f""" Similarly, during the execution of the same test input on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}', a value it never attains in version 'original'."""
                        elif acc_unique_var_state is not None:
                            prompt += f"""When the above test input is executed on version 'patched', the variable '{acc_unique_var_state[0]}' is assigned the value '{acc_unique_var_state[1]}'. However, this variable never attains this value in version 'original'."""
                        
                        prompt += f"""The identical output for this sample test input is: {existing_test_accepted_output}
"""
                prompt += f"""
Your task is to generate a new test input in Python dict format as follows:
```python
{self.test_format}
```
This test input should be designed such that it exposes the differences between the two versions 'original' and 'patched'. In other words, when the test input is given to versions 'original' and 'patched', they should produce different outputs. This can be represented as:
```python
original(inputdata) != patched(inputdata)
```
Please note that your output should not contain any explanation or newline ('\\n') characters. If the function takes multiple inputs, input them all as a tuple to the 'inputdata' field. Create a 'difference exposing test' input as per the Python dict format above.
"""

            chatgpt_resp = await self.chatgpt.get_response(new_question=prompt, author_id=author_id, problem_id=problem_id)
            for i in range(len(chatgpt_resp)):
                responses.append(chatgpt_resp[i])
            
            self.prompt_history.append((prompt, responses[0]))
        #print the responses
        #print(f"###CHATRESP###\n\n {responses}")
        #logging.info(f"###CHATRESP###\n\n {responses}")
        if self.is_qb:
            return [self.extract_regex_qb(str(response)) for response in responses]
        else:
            return [self.extract_regex(str(response)) for response in responses]