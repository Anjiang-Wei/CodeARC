from typing import List

def max_adjacent_product(array: List[int]) -> int:
    # Calculate the maximum product of adjacent elements
    return max(a * b for a, b in zip(array, array[1:]))

