def solution(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> solution([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> solution([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * i for i in range(1, len(xs))]

