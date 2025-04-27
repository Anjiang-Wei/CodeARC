def round_to_nearest_multiple(n: int, m: int) -> int:
    # Calculate the remainder of n divided by m
    remainder = n % m
    # Check if the remainder is exactly half of m
    if remainder == m / 2:
        return n
    # Otherwise, round n to the nearest multiple of m
    return m * round(n / m)

