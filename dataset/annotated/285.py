def has_lonely_one(n: int) -> bool:
    def loneliest(n: int) -> bool:
        a = list(map(int, str(n)))
        b = [(sum(a[max(0, i - x):i + x + 1]) - x, x) for i, x in enumerate(a)]
        return (min(b)[0], 1) in b

    return loneliest(n)

