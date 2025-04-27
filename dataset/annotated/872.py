def calculate_sorted_expression(s: str) -> int:
    from functools import reduce
    from itertools import cycle
    from operator import add, truediv, mul, sub

    xs = sorted(s.split(), key=lambda x: next(c for c in x if c.isalpha()))
    xs = [int(''.join(filter(str.isdigit, x))) for x in xs]
    ops = cycle([add, sub, mul, truediv])
    return round(reduce(lambda a, b: next(ops)(a, b), xs))

