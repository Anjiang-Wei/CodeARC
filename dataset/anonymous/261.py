def solution(deg, r, precision=10):
    from math import cos, sin, radians
    x, y = r * cos(radians(deg)), r * sin(radians(deg))
    return round(x, precision), round(y, precision)

