def last_decimal_digit(base: int, exponent: int) -> int:
    # Calculate the last decimal digit of base^exponent using modular exponentiation
    return pow(base, exponent, 10)

