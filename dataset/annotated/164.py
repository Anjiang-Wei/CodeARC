from typing import List

def total_nested_list_sum(nested_list: List[List[int]]) -> int:
    return sum(map(sum, nested_list))

