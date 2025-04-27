def solution(S, D):
    from math import floor
    # Calculate the group size on the D-th day
    return floor((2 * D + S * (S - 1)) ** 0.5 + 0.5)

