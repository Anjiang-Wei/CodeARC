import re
from typing import Optional, Tuple

def search_pattern_in_text(text: str, pattern: str) -> Optional[Tuple[str, int, int]]:
    match = re.search(pattern, text)
    if match is None:
        return None
    s = match.start()
    e = match.end()
    return (match.re.pattern, s, e)

