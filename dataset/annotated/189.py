from typing import List

def is_all_elements_identical(arr: List[int]) -> bool:
    return arr.count(arr[0]) == len(arr)

