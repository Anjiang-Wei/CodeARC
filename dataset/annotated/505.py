def sorted_pair_or_empty(m: int, n: int) -> list:
    if m < n:
        m, n = n, m
    if n == 0:
        return []

