import re

def is_lowercase_underscore(text: str) -> bool:
    return bool(re.match('^[a-z]+(_[a-z]+)*$', text))

