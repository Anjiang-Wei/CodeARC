from typing import List

def has_even_number(arr: List[int]) -> bool: 
    return any(x % 2 == 0 for x in arr)

