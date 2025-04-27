def calculate_permutation_value(perm: str) -> int:
    from functools import reduce
    return reduce(lambda t, c: t * 26 + ord(c) - 97, perm, 0) + 1

