def are_anagrams(s: str, t: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    """
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in map(chr, range(97, 123)):
        if s.count(i) != t.count(i):
            return False
    return True

