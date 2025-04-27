def calculate_half_life(quantityInitial: float, quantityRemaining: float, time: float) -> float:
    from math import log
    # Calculate the half-life using the formula: t / log2(N0/N)
    return time / log(quantityInitial / quantityRemaining, 2)

