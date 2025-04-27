def count_mismatches(a: str, b: str) -> int:
    return sum(c != d for c, d in zip(a, b))

