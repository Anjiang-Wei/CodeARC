import re
from typing import Optional, Tuple

def find_first_occurrence(text: str, pattern: str) -> Optional[Tuple[str, int, int]]:
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        return (text[s:e], s, e)
    return None

