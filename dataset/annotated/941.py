def has_repeated_adjacent_character(s: str) -> bool:
    import re
    # Use regex to find any character followed by the same character
    return bool(re.search(r"(.)\1", s.lower()))

