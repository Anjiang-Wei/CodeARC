def calculate_slope(p1: tuple[int, int], p2: tuple[int, int]) -> float | None:
    # Check if the line is vertical or the points are the same
    if p1[0] == p2[0]:
        return None
    # Calculate the slope
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

