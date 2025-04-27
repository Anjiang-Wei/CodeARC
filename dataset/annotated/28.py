def polynomial_derivative(coefficients: list[int]) -> list[int]:
    """Coefficients represent a polynomial.
    coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> polynomial_derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> polynomial_derivative([1, 2, 3])
    [2, 6]
    """
    return [coefficients[i] * i for i in range(1, len(coefficients))]

