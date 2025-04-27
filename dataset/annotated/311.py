def evaluate_polynomial_at_x(poly: list, x: int) -> float:
    from functools import reduce
    from math import factorial

    def aCb(a: int, b: int) -> float:
        # Calculate the binomial coefficient aCb
        return reduce(lambda x, y: x * y, (a - i for i in range(b)), 1) / factorial(b)

    # Calculate the polynomial value at x
    result = sum(n * aCb(x, i) for i, n in enumerate(poly[::-1]))
    
    # Round the result to two significant digits
    return round(result, 2)

