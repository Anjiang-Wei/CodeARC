from typing import List

def calculate_product_remainder(arr: List[int], n: int) -> int: 
    from functools import reduce
    return reduce(lambda x, y: x * y, arr) % n

