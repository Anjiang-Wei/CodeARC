def are_all_characters_same(s: str) -> bool:
    return all(ch == s[0] for ch in s[1:])

