import os
import subprocess
from functools import wraps
import time
import logging


def write_to_file(directory, filename, content):
    """
    Writes content to a file in the specified directory.
    If the directory does not exist, it will be created.
    """
    try:
        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        with open(filepath, "w+") as f:
            f.write(content)
        print(f"File '{filename}' written successfully at '{directory}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def run_process(command, timeout=2):
    try:
        start_time = time.time()
        result = subprocess.run(command, capture_output=True, timeout=timeout)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print(f"Subprocess run_command2, {elapsed_time}, {cmd}")
        return result

    except subprocess.TimeoutExpired as e:
        return "Timeout"
    except Exception as e:
        return str(e)


def retry_decorator(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    logging.info(f"Exception occurred: {e}")
                    retry_count += 1
                    print(
                        f"Retrying... (Attempt {retry_count} of {max_retries})")
                    logging.info(
                        f"Retrying... (Attempt {retry_count} of {max_retries})"
                    )
                    time.sleep(delay)
            print(f"Max retries reached. Giving up.")
            logging.info(f"Max retries reached. Giving up.")

        return wrapper

    return decorator

def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    with open(file_path, "r", encoding='utf-8') as file:
        contents = file.read()
    return contents