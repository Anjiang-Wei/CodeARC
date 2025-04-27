def find_quadratic_coefficients(x1: float, x2: float) -> tuple:
    # Coefficients of the quadratic equation are calculated based on the roots x1 and x2
    # a is fixed to 1
    # b is the negative sum of the roots
    # c is the product of the roots
    return (1, -x1 - x2, x1 * x2)

