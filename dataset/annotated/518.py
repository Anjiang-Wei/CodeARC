def calculate_remainder(dividend: int, divisor: int) -> int:
    while divisor <= dividend:
        dividend = dividend - divisor
    return dividend

