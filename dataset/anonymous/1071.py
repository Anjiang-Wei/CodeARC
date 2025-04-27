def solution(s):
    return next(c for c in s if s.count(c) == 1)

