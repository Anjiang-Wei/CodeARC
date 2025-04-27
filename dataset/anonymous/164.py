from typing import List

def solution(test_list: List[List[int]]) -> int:
    return sum(map(sum, test_list))

