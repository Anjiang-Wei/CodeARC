import re
from typing import Optional, Match

def find_pattern_start_a_end_b(text: str) -> Optional[Match[str]]:
    patterns = 'a.*?b$'
    return re.search(patterns, text)

