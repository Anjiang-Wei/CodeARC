def solution(f0, p, c0, n, i):
    for _ in range(n-1):
        f0 = int(f0 * (100 + p) / 100 - c0)
        c0 = int(c0 * (100 + i) / 100)
        if f0 < 0:
            return False
    return True

