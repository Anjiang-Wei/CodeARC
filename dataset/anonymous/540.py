def solution(x):
    MATCH = int('10' * 16, 2)
    return bool(MATCH & x)

