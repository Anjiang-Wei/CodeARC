import re

def contains_ab_with_two_or_three_bs(text: str) -> bool:
    patterns = 'ab{2,3}'
    return re.search(patterns, text) is not None

