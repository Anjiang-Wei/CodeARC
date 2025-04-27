from typing import List

def sum_of_powers(r: List[int]) -> int:
    return sum(2**i for i in r)

