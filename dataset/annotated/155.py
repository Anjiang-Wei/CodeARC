from typing import List

def calculate_unique_product(list_data: List[int]) -> int:
    from functools import reduce
    return reduce(lambda x, y: x*y, set(list_data))

