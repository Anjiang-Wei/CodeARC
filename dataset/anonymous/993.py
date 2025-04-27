def solution(n, m):
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'

