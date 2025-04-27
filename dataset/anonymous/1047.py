def solution(a, r, n):
    return ', '.join(str(a + b * r) for b in range(n))

