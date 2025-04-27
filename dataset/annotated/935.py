def count_matching_pairs(n: int, sequence: list) -> int:
    return sum(a == b for a, b in zip(sequence, sequence[n:]))

