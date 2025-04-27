import re

def replace_special_chars_with_colon(text: str) -> str:
    return re.sub("[ ,.]", ":", text)

