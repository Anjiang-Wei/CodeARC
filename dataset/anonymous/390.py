def solution(k, n, m, x):
    def sim(k, n, p):
        r = [(k, k, 0), (k, p, p)]
        for i in range(n - 2):
            u, d = r[0][1] + r[1][1], r[1][1]
            r = [r[1], (r[1][0] + u - d, u, d)]
        return r[1][0]

    z, o = sim(k, n - 1, 0), sim(k, n - 1, 1)
    return sim(k, x, (m - z) // (o - z))

