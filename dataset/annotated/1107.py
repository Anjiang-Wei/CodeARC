def calculate_cone_volume(r: float, h: float) -> float:
    from math import pi
    # Calculate the volume of the cone using the formula (1/3) * π * r^2 * h
    # Use floor division to round down to the nearest integer
    return pi * r**2 * h // 3

