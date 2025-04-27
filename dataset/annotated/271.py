def are_pairs_within_limit(a: list[int]) -> bool:
    return all(a[i] + a[-i-1] <= 10 for i in range(len(a) // 2))

