def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    res, base = 1, base % modulus
    while exponent > 0:
        if exponent & 1:
            res = res * base % modulus
        exponent >>= 1
        base = base * base % modulus
    return res

