def has_adjacent_duplicates(s: str) -> bool:
    return any(m == n for m, n in zip(s, s[1:]))

