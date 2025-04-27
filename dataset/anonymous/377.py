def solution(r):
    import numpy
    # If there are roots, calculate the polynomial coefficients using numpy.poly
    # Reverse the list to match the required order
    # If no roots, return the identity polynomial [1]
    return list(reversed(numpy.poly(tuple(r)))) if len(r) > 0 else [1]

