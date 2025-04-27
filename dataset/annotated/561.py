def calculate_water_volume(h: float, d: float, vt: int) -> int:
    import math
    
    r = d / 2.0
    if h == r:
        return vt // 2  # The tank is half full
    
    half = h > r  # Check if more than half full
    h = d - h if half else h  # Adjust h accordingly
    a = r - h  # Perpendicular intercept of the chord
    b = math.sqrt(r**2 - a**2)  # Half the chord
    t = 2 * math.asin(b / r)  # Angle the chord sweeps out
    A = r**2 * t / 2 - b * a  # Area of the segment
    v = vt * A / (math.pi * r**2)  # Volume of the segment
    
    return int(vt - v) if half else int(v)

