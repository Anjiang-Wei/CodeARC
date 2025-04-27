def have_same_unique_pattern(string1: str, string2: str) -> bool:
    return len(set(string1)) == len(set(string2)) == len(set(zip(string1, string2)))

