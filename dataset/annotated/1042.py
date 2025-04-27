def calculate_max_mistakes(n: int, time: int) -> int:
    from math import log
    # Calculate the maximum number of mistakes Alex can afford
    return int(log((time - n * 6) / 5 + 1, 2))

