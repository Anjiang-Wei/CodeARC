import re
from typing import Optional, Match

def match_three_consecutive_bs(text: str) -> Optional[Match[str]]:
    patterns = 'ab{3}?'
    return re.search(patterns, text)

