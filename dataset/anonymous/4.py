def solution(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> solution(3, 5)
    1
    >>> solution(25, 15)
    5
    """
    return a if b == 0 else solution(b, a % b)

