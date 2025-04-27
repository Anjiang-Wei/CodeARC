def solution(line):
    from itertools import groupby
    
    merged = []
    for k, g in groupby(v for v in line if v):
        g = list(g)
        n, r = divmod(len(g), 2)
        if n:
            merged.extend([k * 2] * n)
        if r:
            merged.append(k)
    
    return merged + [0] * (len(line) - len(merged))

