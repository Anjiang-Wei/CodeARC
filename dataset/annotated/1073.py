def reduce_values(a: int, b: int) -> list[int]:
    if not (a and b):
        return [a, b]
    if a >= 2 * b:
        return reduce_values(a % (2 * b), b)
    if b >= 2 * a:
        return reduce_values(a, b % (2 * a))
    return [a, b]

