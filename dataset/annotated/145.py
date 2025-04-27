from typing import List

def are_numbers_consecutive(lst: List[int]) -> bool:
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

