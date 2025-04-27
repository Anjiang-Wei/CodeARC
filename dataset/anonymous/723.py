from typing import List

def solution(nums: List[int]) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    possibility_flag = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if possibility_flag:
                return False
            possibility_flag = True
            # Check if we can adjust the current or previous element
            if (i-2 < 0 or nums[i-2] <= nums[i]) or (i+1 >= len(nums) or nums[i+1] >= nums[i-1]):
                continue
            else:
                return False
    return True

