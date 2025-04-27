def integrate_polynomial(coef: int, exp: int) -> str:
    exp = exp + 1
    coef = coef / exp if coef % exp else coef // exp
    return f"{coef}x^{exp}"

