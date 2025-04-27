def count_lowercase_letters(s: str) -> int:
    return sum(a.islower() for a in s)

