from typing import List

def max_successive_difference(numbers: List[int]) -> int:
    lst = sorted(numbers)
    # Calculate the maximum difference between successive elements
    return max(b - a for a, b in zip(lst, lst[1:]))

