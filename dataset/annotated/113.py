from typing import List

def sum_even_numbers_at_even_indices(arr: List[int]) -> int:  
    return sum(x for x in arr[::2] if x % 2 == 0)

