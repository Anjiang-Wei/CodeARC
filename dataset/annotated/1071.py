def find_first_unique_char(s: str) -> str:
    return next(c for c in s if s.count(c) == 1)

