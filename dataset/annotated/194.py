from typing import List

def all_odd_at_odd_indices(nums: List[int]) -> bool:
    return all(n % 2 == 1 for n in nums[1::2])

