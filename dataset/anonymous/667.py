def solution(n, x, a):
    from functools import reduce
    # Calculate the probability that Peter doesn't drink a laxative shot
    probability = reduce(lambda m, b: m * (1 - x / (n - b)), range(a), 1)
    # Round the result to two decimal places
    return round(probability, 2)

