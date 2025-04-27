def solution(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

