from typing import List

def power_elements(nums: List[int], n: int) -> List[int]:
    nth_nums = list(map(lambda x: x ** n, nums))
    return nth_nums

