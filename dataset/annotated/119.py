def max_sum_subarray_after_repeating(a: list[int], n: int, k: int) -> int:
    modified = a * k
    pre = 0  # dp[i-1]
    res = modified[0]
    for num in modified:
        pre = max(pre + num, num)
        res = max(pre, res)
    return res

