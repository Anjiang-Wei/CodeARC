def calculate_max_sum_increasing_subsequence(
    a: list[int], 
    n: int, 
    index: int, 
    k: int
) -> int:
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if a[i] > a[0]:
            dp[0][i] = a[i] + a[0]
        else:
            dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n):
            if a[j] > a[i] and j > i:
                if dp[i - 1][i] + a[j] > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][i] + a[j]
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[index][k]

