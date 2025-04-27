def calculate_lcm(*args: int) -> int:
    from functools import reduce

    def gcd(a: int, b: int) -> int:
        """Euclidean Algorithm"""
        return b if a == 0 else gcd(b % a, a)

    def lcms(a: int, b: int) -> int:
        return (a * b) // gcd(a, b)

    return reduce(lcms, args) if args else 1

