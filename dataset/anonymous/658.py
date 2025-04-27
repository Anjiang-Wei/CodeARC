def solution(s):
    from math import ceil
    
    if not s:
        return "name must be at least one letter"
    
    x = ceil(len(s) ** 0.5)
    it = iter(s.ljust(x * x, '.'))
    
    return [[next(it) for _ in range(x)] for _ in range(x)]

