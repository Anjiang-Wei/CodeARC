from typing import List

def rotate_array(arr: List[int], n: int) -> List[int]:
    # Calculate the effective rotation
    n = n % len(arr)
    # Rotate the array by slicing
    return arr[-n:] + arr[:-n]

