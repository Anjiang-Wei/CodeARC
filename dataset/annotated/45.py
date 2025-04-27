def multiply_unit_digits(a: int, b: int) -> int:
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply_unit_digits(148, 412) should return 16.
    multiply_unit_digits(19, 28) should return 72.
    multiply_unit_digits(2020, 1851) should return 0.
    multiply_unit_digits(14,-15) should return 20.
    """

    return int(str(a)[-1]) * int(str(b)[-1])

