def solution(b, e, m):
    res, b = 1, b % m
    while e > 0:
        if e & 1:
            res = res * b % m
        e >>= 1
        b = b * b % m
    return res

