from typing import List

def find_unique_numbers(nums: List[int]) -> List[int]:
    return [n for n in nums if nums.count(n) == 1]

