def solution(base):
    from operator import mul

    def comb_n(n):
        c = 1
        for k in range(0, n + 1):
            yield c
            c = c * (n - k) // (k + 1)

    return sum(map(mul, base, comb_n(len(base) - 1)))

