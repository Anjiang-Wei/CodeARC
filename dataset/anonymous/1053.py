def solution(m):
    from bisect import bisect_left

    def sierpinski():
        x = s = 0
        while True:
            for a in 4, 9, 56, 61:
                s += x + a
                yield s
            x += 65

    s = sierpinski()
    S = [next(s)]

    while S[-1] < m:
        S.append(next(s))
    
    i = bisect_left(S, m)
    
    # Return the closest value to m, preferring the larger one in case of a tie
    return min(S[i:i-2:-1], key=lambda n: abs(m - n))

