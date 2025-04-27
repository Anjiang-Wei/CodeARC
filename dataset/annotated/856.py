from typing import List

def get_nth_smallest_element(arr: List[int], pos: int) -> int:
    return sorted(arr)[pos-1]  # Return the Nth smallest element

