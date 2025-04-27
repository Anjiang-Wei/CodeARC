def find_numbers_from_sum_and_difference(sum: float, difference: float) -> tuple[float, float] | None:
    x = (sum + difference) / 2
    y = (sum - difference) / 2
    # Check for invalid conditions
    if sum < 0 or difference < 0 or x < 0 or y < 0:
        return None
    return (x, y)

