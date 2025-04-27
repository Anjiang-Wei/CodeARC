def calculate_gcd(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> calculate_gcd(3, 5)
    1
    >>> calculate_gcd(25, 15)
    5
    """
    return a if b == 0 else calculate_gcd(b, a % b)

