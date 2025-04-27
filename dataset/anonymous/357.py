def solution(s1, s2):
    return len(set(zip(s1, s2))) == len(set(s1)) == len(set(s2))

