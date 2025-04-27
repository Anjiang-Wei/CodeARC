from .utils import write_to_file
import os
import json
from dotenv import load_dotenv
import logging
import asyncio
import sys
import inspect
from pathlib import Path

# Add SynBench to path to import llm_generate
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))))
from llm_generate import generate_openai_multisample, EvalInput

load_dotenv()
MAX_LENGTH = 39000


class ChatGPT_2():

    def __init__(self, default_instruction, cache_file_path, default_temp, default_n):
        self.default_instruction = default_instruction
        self.cache_file_path = cache_file_path
        self.cache = self.load_cache()  # Load cache from file
        self.default_temp = default_temp
        self.default_n = default_n
        self.default_instruction = default_instruction

    def load_cache(self):
        if os.path.exists(self.cache_file_path):
            with open(self.cache_file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        Path(self.cache_file_path).parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        with open(self.cache_file_path, 'w') as f:
            json.dump(self.cache, f)

    async def get_response(self, new_question, previous_questions_and_answers=None, author_id=None, problem_id=None, temp=None, n=None, instruction=None):
        messages = [
            {"role": "system",
                "content": instruction if instruction else self.default_instruction},
        ]
        if previous_questions_and_answers:
            for question, answer in previous_questions_and_answers:
                messages.append({"role": "user", "content": question})
                messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": new_question})

        logging.info(f"###CHATGPT_INITIAL_PROMPT###\n\n {messages}")

        prompt = "\n".join([msg['content'] for msg in messages])

        while len(prompt) > MAX_LENGTH:
            # Remove messages from the start until the length is below the threshold
            messages = messages[:3] + messages[5:]
            prompt = "\n".join([msg['content'] for msg in messages])

        if prompt in self.cache:
            return self.cache[prompt]

        input_obj = EvalInput(messages=messages, model_with_platform="openai/gpt-4o-mini-2024-07-18")
        responses = await generate_openai_multisample(input_obj, n if n else self.default_n, temp if temp else self.default_temp)
        self.cache[prompt] = responses
        self.save_cache()  # Save cache to file
        return responses