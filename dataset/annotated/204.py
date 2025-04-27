def check_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    return n**(1/2) == int(n**(1/2))

