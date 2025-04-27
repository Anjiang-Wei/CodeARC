from typing import List

def solution(nums: List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Remove duplicates and sort the numbers
    nums = sorted(list(set(nums)))
    
    # Check if there are less than 3 distinct numbers
    if len(nums) < 3:
        # Return the maximum number if third maximum doesn't exist
        return max(nums)
    else:
        # Return the third maximum number
        return nums[-3]

