from typing import List

def max_distance_between_matches(arr: List[int]) -> int:
    # Calculate the greatest distance between matching numbers in the array
    return max(i - arr.index(x) for i, x in enumerate(arr))

