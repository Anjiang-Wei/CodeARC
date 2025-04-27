def solution(*ages):
    import math
    # Calculate the sum of squares of ages
    sum_of_squares = sum(a * a for a in ages)
    # Take the square root of the sum
    sqrt_result = math.sqrt(sum_of_squares)
    # Divide by 2 and return the floored result
    return int(sqrt_result // 2)

