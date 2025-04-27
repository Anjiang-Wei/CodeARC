def compute_polynomial_coefficients(r: list[float]) -> list[float]:
    import numpy
    return list(reversed(numpy.poly(tuple(r)))) if len(r) > 0 else [1]

