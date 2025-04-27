from typing import List

def sort_by_bits(arr: List[int]) -> List[int]:
    # Sort the array based on the number of 'on' bits and then by the integer value
    return sorted(arr, key=lambda x: (bin(x).count("1"), x))

