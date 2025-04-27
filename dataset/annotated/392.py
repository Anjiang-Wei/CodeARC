from typing import List

def generate_power_set(nums: List[int]) -> List[List[int]]:
    from itertools import compress, product
    
    # Generate all combinations of inclusion/exclusion for each element
    return [list(compress(nums, p)) for p in product((0, 1), repeat=len(nums))]

