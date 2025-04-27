from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    sum = max_sum = 0
    for n in arr:
        sum = max(sum + n, 0)
        max_sum = max(sum, max_sum)
    return max_sum

