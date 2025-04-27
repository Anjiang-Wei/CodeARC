def count_non_forbidden_numbers(n: int) -> int:
    return sum(not ('4' in s or '7' in s) for s in map(str, range(0, n+1, 13)))

