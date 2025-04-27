def find_longest_common_subsequence(x: str, y: str) -> str:
    def lcs(x: str, y: str) -> str:
        if len(x) == 0 or len(y) == 0:
            return ''
        if x[-1] == y[-1]:
            return lcs(x[:-1], y[:-1]) + x[-1]
        else:
            lcs1 = lcs(x, y[:-1])
            lcs2 = lcs(x[:-1], y)
            return lcs1 if len(lcs1) > len(lcs2) else lcs2

    return lcs(x, y)

