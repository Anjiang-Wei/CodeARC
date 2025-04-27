from typing import List

def adjust_with_remainder(nums: List[int], div: int) -> List[int]:
    return [x + x % div for x in nums]

