def solution(n, d, ang, dist_mult, ang_mult):
    from math import cos, sin, radians
    
    x, y, a = 0, 0, radians(ang)
    for i in range(n):
        x += d * cos(a)
        y += d * sin(a)
        d *= dist_mult
        a *= ang_mult
    
    return x, y

