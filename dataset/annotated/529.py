from typing import List

def calculate_absolute_product_difference(a: List[int], b: List[int]) -> int:
    from numpy import prod
    return abs(prod(a) - prod(b))

