def solution(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> solution(8, 3)
    '22'
    >>> solution(8, 2)
    '1000'
    >>> solution(7, 2)
    '111'
    """
    if x == 0: return "0"
    ret = ""
    while x != 0:
        ret = str(x % base) + ret
        x //= base
    return ret

