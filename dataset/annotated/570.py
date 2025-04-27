def convert_to_fraction_parts(fraction: tuple[int, int]) -> tuple[int, int]:
    from fractions import Fraction
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)

