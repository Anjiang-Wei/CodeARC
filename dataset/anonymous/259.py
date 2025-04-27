def solution(sequence):
    def f(X):
        return [list(x) for x in zip(*X[::-1])]

    def g(X):
        return [list(x) for x in zip(*X)][::-1]

    def ROTF(U, L, F, R, B, D):
        U[2], (L[0][2], L[1][2], L[2][2]), (R[0][0], R[1][0], R[2][0]), D[0] = (
            [L[0][2], L[1][2], L[2][2]][::-1],
            list(D[0]),
            list(U[2]),
            [R[0][0], R[1][0], R[2][0]][::-1]
        )
        return (U, L, f(F), R, B, D)

    def ROTS(U, L, F, R, B, D):
        U[1], (L[0][1], L[1][1], L[2][1]), (R[0][1], R[1][1], R[2][1]), D[1] = (
            [L[0][1], L[1][1], L[2][1]][::-1],
            list(D[1]),
            list(U[1]),
            [R[0][1], R[1][1], R[2][1]][::-1]
        )
        return (U, L, F, R, B, D)

    c = "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww"
    U, L, F, R, B, D = ([list(c[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))

    A = []
    for x in sequence.replace("'", '3').split():
        A += [x[0]] * int(x[1]) if len(x) == 2 else [x]

    T = []
    W = 'FS YYYFY YYYFSY YFYYY YFSYYY YYFYY YYFSYY XFXXX XFSXXX XXXFX XXXFSX YYYSY XSXXX'
    for x in A:
        T += {k: list(v) for k, v in zip('fLlRrBbDdUuME', W.split())}.get(x, x)

    for X in T:
        if X == 'X':
            (U, L, F, R, B, D) = (F, g(L), D, f(R), g(g(U)), g(g(B)))
        if X == 'Y':
            (U, L, F, R, B, D) = (f(U), F, R, B, L, g(D))
        if X == 'Z':
            (U, L, F, R, B, D) = (f(L), f(D), f(F), f(U), g(B), f(R))
        if X == 'F':
            (U, L, F, R, B, D) = ROTF(U, L, F, R, B, D)
        if X == 'S':
            (U, L, F, R, B, D) = ROTS(U, L, F, R, B, D)

    return ''.join(''.join(''.join(y) for y in x) for x in (U, L, F, R, B, D))

