from typing import List

def sum_of_even_numbers(seq: List[int]) -> int:
    return sum(n for n in seq if not n % 2)

