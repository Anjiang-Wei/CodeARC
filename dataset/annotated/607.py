def calculate_truncated_cone_volume(d1: float, d2: float, h: float) -> float:
    from math import pi
    # Calculate the volume using the formula for a truncated cone
    volume = h / 12.0 * pi * (d1**2 + d1*d2 + d2**2)
    # Return the volume rounded to 2 decimal places
    return round(volume, 2)

