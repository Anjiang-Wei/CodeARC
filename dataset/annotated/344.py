def calculate_final_position(n: int, d: float, ang: float, dist_mult: float, ang_mult: float) -> tuple[float, float]:
    from math import cos, sin, radians
    
    x, y, a = 0, 0, radians(ang)
    for i in range(n):
        x += d * cos(a)
        y += d * sin(a)
        d *= dist_mult
        a *= ang_mult
    
    return x, y

