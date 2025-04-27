def solution(n, time):
    from math import log
    # Calculate the maximum number of mistakes Alex can afford
    return int(log((time - n * 6) / 5 + 1, 2))

