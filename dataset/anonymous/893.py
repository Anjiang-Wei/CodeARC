from typing import List

def solution(nums: List[int], target: int) -> int:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Create a list of numbers less than the target
    num = [i for i in nums if i < target]
    # Return the length of this list, which is the index where the target would be inserted
    return len(num)

