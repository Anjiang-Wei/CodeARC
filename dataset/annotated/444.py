def can_construct_from_chars(s1: str, s2: str) -> bool:
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

