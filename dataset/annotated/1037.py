def is_in_sharkovsky_order(a: int, b: int) -> bool:
    def f(n: int, p: int = 0) -> tuple:
        while n % 2 == 0:
            n >>= 1
            p += 1
        return n == 1, p * (-1) ** (n == 1), n

    # Compare the Sharkovsky order of a and b
    return f(a) < f(b)

