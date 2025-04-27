from bisect import bisect_right
from typing import List

def find_right_insertion_index(a: List[int], x: int) -> int:
    return bisect_right(a, x)

