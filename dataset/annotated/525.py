def sum_of_reduced_fraction_parts(a: int, b: int) -> int:
    from math import gcd
    # Calculate the greatest common divisor
    common_divisor = gcd(a, b)
    # Reduce the fraction and return the sum of the numerator and denominator
    return (a // common_divisor) + (b // common_divisor)

