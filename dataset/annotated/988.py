from typing import List

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # Use a dictionary to store the last index of each number
    index_map = {}
    
    for i, num in enumerate(nums):
        # If the number is already in the dictionary and the difference of indices is at most k
        if num in index_map and i - index_map[num] <= k:
            return True
        # Update the last index of the number
        index_map[num] = i
    
    return False

