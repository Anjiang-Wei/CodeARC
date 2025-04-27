def count_consecutive_characters(s: str) -> list[list[int, str]]:
    from itertools import groupby
    
    # Group the string by consecutive characters and count occurrences
    return [[sum(1 for _ in g), c] for c, g in groupby(s)]

