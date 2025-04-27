def solution(numerator, denominator):
    from fractions import Fraction as BaseFraction
    from math import gcd

    class Fraction:
        def __init__(self, numerator, denominator):
            if denominator == 0:
                raise ValueError("Denominator cannot be zero.")
            common = gcd(numerator, denominator)
            self.numerator = numerator // common
            self.denominator = denominator // common

        def to_decimal(self):
            return self.numerator / self.denominator

        def __str__(self):
            n, d = self.numerator, self.denominator
            s, w, n = "-" if n < 0 else "", *divmod(abs(n), d)
            r = " ".join((str(w) if w else "", f"{n}/{d}" if n else "")).strip()
            return f"{s}{r}"

        def __add__(self, other):
            if isinstance(other, int):
                other = Fraction(other, 1)
            n = self.numerator * other.denominator + other.numerator * self.denominator
            d = self.denominator * other.denominator
            return Fraction(n, d)

        def __sub__(self, other):
            if isinstance(other, int):
                other = Fraction(other, 1)
            n = self.numerator * other.denominator - other.numerator * self.denominator
            d = self.denominator * other.denominator
            return Fraction(n, d)

        def __mul__(self, other):
            if isinstance(other, int):
                other = Fraction(other, 1)
            n = self.numerator * other.numerator
            d = self.denominator * other.denominator
            return Fraction(n, d)

        def __truediv__(self, other):
            if isinstance(other, int):
                other = Fraction(other, 1)
            n = self.numerator * other.denominator
            d = self.denominator * other.numerator
            if d == 0:
                raise ZeroDivisionError("division by zero")
            return Fraction(n, d)

    return Fraction(numerator, denominator)

