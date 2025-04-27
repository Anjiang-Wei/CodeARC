def count_character_frequency(s: str) -> dict[str, int]:
    from collections import Counter
    # Count occurrences of each character in the string
    return dict(Counter(s))

