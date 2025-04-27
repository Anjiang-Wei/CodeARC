import cmath

def solution(a, b):
    angle = cmath.phase(a + b)
    return angle

