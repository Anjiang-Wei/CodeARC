from typing import List

def list_difference_exclude(a: List[int], b: List[int]) -> List[int]:
    return [x for x in a if x not in b]

