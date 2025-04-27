def weighted_sum(*args: float) -> float:
    # Calculate the sum of each argument multiplied by its (index + 1)
    return sum((i + 1) * v for i, v in enumerate(args))

