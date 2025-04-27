def solution(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in map(chr, range(97, 123)):
        if s.count(i) != t.count(i):
            return False
    return True

