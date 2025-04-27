from typing import List

def count_even_minus_odd(a: List[int]) -> int:
    return sum(1 if v % 2 == 0 else -1 for v in a if isinstance(v, int))

