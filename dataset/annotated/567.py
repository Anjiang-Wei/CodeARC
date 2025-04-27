def calculate_extrapolated_value(
    p1: tuple[float, float], 
    p2: tuple[float, float], 
    x3: float
) -> int:
    from math import log
    (x1, y1), (x2, y2) = p1, p2
    x1 += 1e-9; y1 += 1e-9
    # Calculate y3 using the power law formula
    y3 = y1 * (y2 / y1) ** log(x3 / x1, x2 / x1)
    # Return the result rounded to the nearest integer
    return round(y3)

