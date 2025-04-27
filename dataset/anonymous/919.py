def solution(*args):
    from functools import reduce

    def gcd(a, b):
        """Euclidean Algorithm"""
        return b if a == 0 else gcd(b % a, a)

    def lcms(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcms, args) if args else 1

