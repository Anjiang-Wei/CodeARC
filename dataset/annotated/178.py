import math

def calculate_lateral_surface_area_of_cone(r: float, h: float) -> float:
    l = math.sqrt(r * r + h * h)
    return math.pi * r * l

