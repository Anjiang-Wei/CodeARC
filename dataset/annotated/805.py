def weighted_average_sum(*args: float) -> int:
    # Calculate the sum of each argument divided by its index (starting from 1)
    # Round the result and convert to integer
    return int(round(sum(float(a) / i for i, a in enumerate(args, 1))))

