def solution(n, w):
    import math
    e = math.exp(-2)
    # Calculate the weight of n glass walls using the given formula
    return (1 - 3 * e) / (1 - e) / 4 * (1 - e**n) * w

