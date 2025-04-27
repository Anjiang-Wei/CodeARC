def solution(a, n, k):
    modified = a * k
    pre = 0  # dp[i-1]
    res = modified[0]
    for num in modified:
        pre = max(pre + num, num)
        res = max(pre, res)
    return res

