from typing import List

def sum_of_two_smallest(numbers: List[int]) -> int:
    return sum(sorted(numbers)[:2])

