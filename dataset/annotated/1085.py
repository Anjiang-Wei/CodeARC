def has_unique_characters(string: str) -> bool:
    return len(string) == len(set(string.lower()))

