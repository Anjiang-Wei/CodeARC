def sum_inclusive_range(a: int, b: int) -> int:
    return sum(range(min(a, b), max(a, b) + 1))

