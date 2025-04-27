def solution(n):
    res = 0
    while not n & 1:
        res += 1
        n >>= 1
    return res

