def find_modular_inverse(a: int, n: int) -> int | None:
    def egcd(a: int, b: int) -> tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(a, n)
    if g != 1:
        return None
    else:
        return x % n

