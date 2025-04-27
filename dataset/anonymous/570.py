def solution(fraction):
    from fractions import Fraction
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)

