def solution(perm):
    from functools import reduce
    return reduce(lambda t, c: t * 26 + ord(c) - 97, perm, 0) + 1

