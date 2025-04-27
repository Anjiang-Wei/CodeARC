import re
from typing import Callable

def swapcase_repeated_chars(s: str) -> str:
    return re.sub(r'(.)\1+', lambda m: m.group().swapcase(), s)

