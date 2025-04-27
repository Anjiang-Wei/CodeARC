def polar_to_cartesian(deg: float, r: float, precision: int = 10) -> tuple[float, float]:
    from math import cos, sin, radians
    x, y = r * cos(radians(deg)), r * sin(radians(deg))
    return round(x, precision), round(y, precision)

