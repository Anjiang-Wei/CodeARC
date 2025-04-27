# from litellm import completion
import anthropic
import together
import openai

# from litellm import completion
import asyncio
import json
import logging
from functools import wraps

import anthropic
import together
import openai

from enum import Enum
import random
from typing import Optional, List, Dict



class EvalErrorCode(Enum):
    string_above_max_length = "string_above_max_length"
    context_length_exceeded = "context_length_exceeded"
    output_parse_error      = "output_parse_error"
    other_error             = "other_error"

class EvalError(Exception):
    """Custom error type for evaluation."""
    def __init__(self, code: EvalErrorCode, content: Optional[str] = None, inner_error: Optional[Exception] = None):
        if inner_error is not None:
            super().__init__(code, content, *inner_error.args)
        else:
            super().__init__(code, content)
        
        self.code        = code
        self.content     = content
        self.inner_error = inner_error

    def __repr__(self):
        return \
f"""EvalError(
    code        = {self.code}
    content     = {self.content}
    inner_error = (
        type={type(self.inner_error)}
        __str__={self.inner_error}
        args=(
    )
)"""
    
class EvalInput:
    def __init__(self, messages: List[Dict], model_with_platform: str):       
        self._messages             = messages 
        self.model_with_platform  = model_with_platform

    @property
    def model_names(self):
        model_names = self.model_with_platform.split("/")
        assert len(model_names) == 2
        return model_names

    @property 
    def model_platform(self):
        return self.model_names[0]

    @property 
    def model_name(self):
        return self.model_names[1]

    @property
    def messages(self):
        return self._messages
    
    def __repr__(self):
        return \
f"""EvalInput(
    messages = {self._messages}
    model_with_platform = {self.model_with_platform}
)"""




def log_error_wrapper(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as error:
            input = args[0] if args else None
            logging.error(f"""
[Error on Eval] EvalInput = {input}
    [Error Type]
    {type(error)}
    [Error]
    {error}
    [Error.args]
""")
            pass
    return wrapper

def handle_error_openai(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            
            # sleep and cotinue errors
            except (openai.RateLimitError, openai.InternalServerError, openai.APIConnectionError) as error:
                match error.code:
                    case "rate_limit_exceeded":
                        if error.message.find("tokens per min (TPM)") != -1:
                            await asyncio.sleep(60)
                        else:
                            await asyncio.sleep(1)
                        continue
                    case "insufficient_quota":
                        print("Error: Insufficient quota", flush=True)
                        return "[ERROR] Insufficient quota"
                    case _:
                        print("Error: Unknown error", flush=True)
                        return "[ERROR] Unknown error"
            # write EvalError into the pair.eval_error record
            except openai.BadRequestError as error:
                match error.code:
                    case "context_length_exceeded":
                        print("Error: Context length exceeded", flush=True)
                        return "[ERROR] Context length exceeded"
                    case "string_above_max_length":
                        print("Error: String above max length", flush=True)
                        return "[ERROR] String above max length"
                    case _:
                        print("Error: Unknown error", flush=True)
                        return "[ERROR] Unknown error"

            # directly raise
            except openai.AuthenticationError as error:
                raise error
                
            except Exception as error:
                print("Error: Unknown error", flush=True)
                return "[ERROR] Unknown error"
    return wrapper

"""
def handle_error_deepseek(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            
            # sleep and cotinue errors
            except (openai.RateLimitError, openai.InternalServerError, openai.APIConnectionError, openai.BadRequestError) as error:
                match error.code:
                    case "rate_limit_exceeded":
                        if error.message.find("tokens per min (TPM)") != -1:
                            await asyncio.sleep(60)
                        else:
                            await asyncio.sleep(1)
                        continue
                    case "insufficient_quota":
                        raise error
                    case "invalid_request_error":
                        # NOTE: Deepseek API only support 64k tokens
                        if error.message.find("This model's maximum context length is 65536 tokens") != -1:
                            print("Error: This model's maximum context length is 65536 tokens", flush=True)
                            return "Sorry, the model's maximum context length is 65536 tokens."
                    case _:
                        raise error
            # write EvalError into the pair.eval_error record
            except openai.BadRequestError as error:
                match error.code:
                    case "context_length_exceeded":
                        raise EvalError(code=EvalErrorCode.context_length_exceeded, inner_error=error)
                    case "string_above_max_length":
                        raise EvalError(code=EvalErrorCode.string_above_max_length, inner_error=error)
                    case _:
                        raise error

            # directly raise
            # except openai.AuthenticationError as error:
                # raise error
            
            # except Exception as error:
                # raise error
    return wrapper
"""

def handle_error_anthropic(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            
            except anthropic.RateLimitError as error:
                # Error code: 429 - {'type': 'error', 'error': {'type': 'rate_limit_error', 'message': 'This request would exceed your organization’s rate limit of 400,000 input tokens per minute. For details, refer to: https://docs.anthropic.com/en/api/rate-limits; see the response headers for current usage. Please reduce the prompt length or the maximum tokens requested, or try again later. You may also contact sales at https://www.anthropic.com/contact-sales to discuss your options for a rate limit increase.'}}
                match error.body["error"]["type"]:
                    case "rate_limit_error":
                        # sleep and cotinue errors
                        if error.body["error"]["message"].find("tokens per minute") != -1:
                            await asyncio.sleep(60)
                        else:
                            await asyncio.sleep(1)
                        continue
                    case _:
                        print("Error: Unknown error", flush=True)
                        return "[ERROR] Unknown error"

            # directly raise
            # except openai.AuthenticationError as error:
                # raise error
            
            except Exception as error:
                print("Error: Unknown error", flush=True)
                return "[ERROR] Unknown error"
    return wrapper

def handle_error_together(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            except together.error.ServiceUnavailableError as error:
                error_message = error._message[18:]
                match (type(error), error.http_status, error_message):
                    case (together.error.ServiceUnavailableError, 503, "The server is overloaded or not ready yet."):
                        await asyncio.sleep(60)
                        continue
                    case _:
                        print("Error: Unknown error", flush=True)
                        return "[ERROR] Unknown error"
            except (together.error.APIError, together.error.RateLimitError) as error:
                try:
                    error_obj = json.loads(error._message[18:])
                    error_type = error_obj.get("type_")
                    error_msg = error_obj.get("message", "")
                    #if error_obj["type_"] is None and error_obj["message"] == "Internal Server Error":
                    if error_type is None and "Internal Server Error" in error_msg:
                        await asyncio.sleep(60)
                        continue
                    match type(error), error.http_status, error_type:
                        case (together.error.RateLimitError, 429, "model_rate_limit") if "rate limit specific to this model" in error_msg:
                            await asyncio.sleep(60)
                            continue
                        case (together.error.APIError, 500, "server_error") if "Internal server error" in error_msg:
                            await asyncio.sleep(60)
                            continue
                        case (together.error.APIError, 413, "invalid_request_error") if "Request entity too large" in error_msg:
                            return "[ERROR] Request entity too large"
                            # raise EvalError(code=EvalErrorCode.string_above_max_length, inner_error=error)
                            # await asyncio.sleep(60)
                            # continue
                        case _:
                            print("Error: Unknown error", flush=True)
                            return "[ERROR] Unknown error"
                except json.JSONDecodeError as json_error:
                    match type(error), error.http_status:
                        case (together.error.APIError, 502):
                            await asyncio.sleep(60)
                            continue
                        case _:
                            print("Error: Unknown error", flush=True)
                            return "[ERROR] Unknown error"
            except together.error.InvalidRequestError as error:
                error_obj = json.loads(error._message[18:])
                match type(error), error.http_status, error_obj["type_"]:
                    case (together.error.InvalidRequestError, 422, "invalid_request_error") if error_obj["message"].startswith("Input validation error: `inputs` tokens + `max_new_tokens` must be <="):
                        # write EvalError into the pair.eval_error record
                        # raise EvalError(code=EvalErrorCode.context_length_exceeded, inner_error=error)
                        return "[ERROR] Input validation error: `inputs` tokens + `max_new_tokens` must be <="
                    case (together.error.InvalidRequestError, 400, "invalid_request_error") if error_obj["message"] == "Input validation error":
                        # raise EvalError(code=EvalErrorCode.string_above_max_length, inner_error=error)
                        return "[ERROR] Input validation error"
                    case (together.error.InvalidRequestError, 400, "invalid_request_error") if error_obj["message"].startswith("This model\'s maximum context length is "):
                        # raise EvalError(code=EvalErrorCode.context_length_exceeded, inner_error=error)
                        return "[ERROR] Exceeded maximum context length"
                    case (together.error.InvalidRequestError, 400, "invalid_request_error") if error_obj["message"] == "All connection attempts failed":
                        # sleep and cotinue errors
                        await asyncio.sleep(60)
                        continue
                    case (together.error.InvalidRequestError, 400, "invalid_request_error") if error_obj["message"] == "Input validation error":
                        # sleep and cotinue errors
                        # raise EvalError(code=EvalErrorCode.context_length_exceeded, inner_error=error)
                        return "[ERROR] Input validation error"
                    case _:
                        print("Error: Unknown error", flush=True)
                        return "[ERROR] Unknown error"
            except together.error.Timeout as error:
                await asyncio.sleep(1)
                continue
            except together.error.APIConnectionError as error:
                print("Error: API connection error", flush=True)
                await asyncio.sleep(60)
                return "[ERROR] API connection error"
            # directly raise
            except together.error.AuthenticationError as error:
                raise error
            
            except Exception as error:
                print("Error: Unknown error", flush=True)
                return "[ERROR] Unknown error"
    return wrapper

async def llm_generate(input: EvalInput) -> str:
    match input.model_platform:
        case "openai":
            return await generate_openai(input=input)
        case "anthropic":
            return await generate_anthropic(input=input)
        case _:
            return await generate_together(input=input)

@handle_error_openai
@log_error_wrapper
async def generate_openai(input: EvalInput) -> str:
    client = openai.AsyncClient()
    if input.model_name == "o3-mini-high":
        chat_completion = await client.chat.completions.create(
            messages = input.messages,
            model    = "o3-mini",
            reasoning_effort= "high",
            # timeout  = 60 * 5
        )
    else:
        chat_completion = await client.chat.completions.create(
            messages = input.messages,
            model    = input.model_name,
            # timeout  = 60 * 5
        )
    await client.close()
    return chat_completion.choices[0].message.content

@handle_error_openai
@log_error_wrapper
async def generate_openai_multisample(input: EvalInput, n: int, temperature: float) -> List[str]:
    client = openai.AsyncClient()
    chat_completion = await client.chat.completions.create(
        messages = input.messages,
        model    = input.model_name,
        n        = n,
        temperature = temperature,
        # timeout  = 60 * 5
    )
    await client.close()
    return [choice.message.content for choice in chat_completion.choices]

@handle_error_anthropic
@log_error_wrapper
async def generate_anthropic(input: EvalInput) -> str:
    client = anthropic.AsyncClient()
    message = await client.messages.create(
        max_tokens = 8192,
        model      = input.model_name,
        messages   = input.messages
    )
    await client.close()
    return "".join([block.text for block in message.content])

@handle_error_together
@log_error_wrapper
async def generate_together(input: EvalInput) -> str:
    client = together.AsyncClient()
    chat_completion = await client.chat.completions.create(
        messages = input.messages,
        model    = f"{input.model_platform}/{input.model_name}"
    )
    # await client.close()
    return chat_completion.choices[0].message.content

"""
@handle_error_deepseek
@log_error_wrapper
async def generate_deepseek(input: EvalInput) -> str:
    deepseek_api_key = os.environ["DEEPSEEK_API_KEY"]
    deepseek_base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    client = openai.AsyncClient(api_key=deepseek_api_key, base_url=deepseek_base_url)
    chat_completion = await client.chat.completions.create(
        messages = input.messages,
        model    = input.model_name,
        # timeout  = 60 * 5
    )
    return chat_completion.choices[0].message.content

#@handle_aisuide_error
@log_error_wrapper
@async_wrap
def create_completion_aisuite(input: EvalInput) -> str:
    client = aisuite.Client()
    chat_completion = client.chat.completions.create(
        messages = input.messages,
        model    = f"{input.model_platform}:{input.model_name}" 
    )
    return chat_completion.choices[0].message.content
"""