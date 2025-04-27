def is_repeated_substring_pattern(s: str) -> bool:
    return (s + s).find(s, 1) == len(s)

