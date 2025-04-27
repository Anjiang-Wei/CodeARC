def solution(n):
    import math
    # Calculate the number of full staircase rows using the quadratic formula
    return int((math.sqrt(8 * n + 1) - 1) / 2)

