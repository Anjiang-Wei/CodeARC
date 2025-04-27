import cmath

def solution(x, y):
    cn = cmath.polar(complex(x, y))
    cn1 = cmath.rect(2, cmath.pi)
    return (cn, cn1)

