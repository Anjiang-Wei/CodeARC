from typing import List

def total_absolute_differences(array: List[int]) -> int:
    return sum(abs(a - b) for a, b in zip(array, array[1:]))

