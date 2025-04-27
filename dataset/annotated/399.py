from typing import List

def max_non_adjacent_sum(vals: List[int]) -> int:
    a = b = 0
    for n in vals:
        a, b = b, max(a + n, b)
    return max(a, b)

