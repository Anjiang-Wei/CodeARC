def solution(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> solution(3, 5)
    3
    >>> solution(1101, 101)
    2
    >>> solution(0, 101)
    1
    >>> solution(3, 11)
    8
    >>> solution(100, 101)
    1
    """

    res, x = 1, 2
    while n != 0:
        if n % 2 == 1:
            res = res * x % p
        x = x * x % p
        n //= 2
    return res % p

