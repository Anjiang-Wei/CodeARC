def solution(s):
    return any(m == n for m, n in zip(s, s[1:]))

