def solution(a, b):
    def gen(n):
        if n >= 10**16:
            return
        for i in range(10):
            x = 10 * n + i
            if x % sum(map(int, str(x))) == 0:
                yield x
                yield from gen(x)

    from bisect import bisect_left as bl, bisect_right as br

    L = sorted(x for n in range(1, 10) for x in gen(n))
    return L[bl(L, a):br(L, b)]

