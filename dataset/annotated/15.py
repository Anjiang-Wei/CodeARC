def convert_to_base_less_than_ten(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> convert_to_base_less_than_ten(8, 3)
    '22'
    >>> convert_to_base_less_than_ten(8, 2)
    '1000'
    >>> convert_to_base_less_than_ten(7, 2)
    '111'
    """
    if x == 0: return "0"
    ret = ""
    while x != 0:
        ret = str(x % base) + ret
        x //= base
    return ret

