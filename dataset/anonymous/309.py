def solution(n):
    from math import ceil
    from fractions import Fraction as F
    
    f = F(n)
    ff = int(f)
    result = [str(ff)] if ff else []
    f -= ff
    
    while f > 0:
        x = F(1, int(ceil(f**-1)))
        f -= x
        result.append(str(x))
    
    return result

