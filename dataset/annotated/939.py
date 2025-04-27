def calculate_distance(p1: tuple[float, float], p2: tuple[float, float], precision: int = 0) -> float:
    import math
    # Calculate the distance using the distance formula
    distance = math.sqrt(sum((b - a) ** 2 for a, b in zip(p1, p2)))
    # Round the distance to the specified precision
    return round(distance, precision)

