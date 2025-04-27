from typing import List

def count_greater_pairs(nums: List[int]) -> int:
    return sum(a > b for i, a in enumerate(nums) for b in nums[i + 1:])

