import re
from typing import Optional, Match

def starts_with_vowel(string: str) -> Optional[Match[str]]: 
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    return re.search(regex, string)

