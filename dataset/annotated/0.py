def get_decimal_part(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> get_decimal_part(3.5)
    0.5
    """
    return number - int(number)

