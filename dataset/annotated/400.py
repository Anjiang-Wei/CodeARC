def find_solution_greater_than_k(start_value: int, k: int) -> int:
    from collections import defaultdict
    from bisect import bisect

    def sum_part(n: int) -> int:
        m, p, q, r, s = 1, 1, 1, 0, n
        while n > 9:
            n, d = divmod(n, 10)
            r += d * p
            p *= 10
            if d:
                m = 1
            else:
                m *= 2
            s += q * n + m * memo[r]
            q *= 2
        return s

    qualified = defaultdict(list)
    memo = {n: n for n in range(10)}
    for n in range(10, 10 ** 6):
        memo[n] = sum_part(n)
        if memo[n] > n:
            k_val, r = divmod(n, memo[n] - n)
            if not r:
                qualified[k_val].append(memo[n] - n)

    return qualified[k][bisect(qualified[k], start_value + 1)]

