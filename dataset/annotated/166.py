def largest_divisible_subset_length(a: list[int]) -> int:
    n = len(a)
    dp = [0 for _ in range(n)]
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        mxm = 0
        for j in range(i + 1, n):
            if a[j] % a[i] == 0 or a[i] % a[j] == 0:
                mxm = max(mxm, dp[j])
        dp[i] = 1 + mxm
    return max(dp)

