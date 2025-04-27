from typing import List

def sum_with_alternate_squares(arr: List[int]) -> int:
    return sum(x**2 if i % 2 == 1 else x for i, x in enumerate(arr))

