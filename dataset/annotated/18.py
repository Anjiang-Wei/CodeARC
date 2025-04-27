def power_mod_2n(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> power_mod_2n(3, 5)
    3
    >>> power_mod_2n(1101, 101)
    2
    >>> power_mod_2n(0, 101)
    1
    >>> power_mod_2n(3, 11)
    8
    >>> power_mod_2n(100, 101)
    1
    """

    res, x = 1, 2
    while n != 0:
        if n % 2 == 1:
            res = res * x % p
        x = x * x % p
        n //= 2
    return res % p

