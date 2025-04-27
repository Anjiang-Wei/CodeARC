def solution(quantityInitial, quantityRemaining, time):
    from math import log
    # Calculate the half-life using the formula: t / log2(N0/N)
    return time / log(quantityInitial / quantityRemaining, 2)

