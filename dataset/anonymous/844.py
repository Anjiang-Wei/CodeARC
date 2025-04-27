from typing import List

def solution(nums: List[int]) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    num_set = set(nums)
    # If the length of the set is the same as the list, there are no duplicates
    return len(nums) != len(num_set)

