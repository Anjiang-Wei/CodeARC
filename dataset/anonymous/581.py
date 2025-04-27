def solution(n):
    from math import ceil, floor
    
    left, right = (len(part) for part in str(n).split("."))
    
    if left < right:
        return ceil(n)
    elif left > right:
        return floor(n)
    else:
        return round(n)

