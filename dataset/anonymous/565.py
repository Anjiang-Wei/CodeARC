def solution(lst, n):
    if n < 0:
        return solution(lst[::-1], 3 - n)
    if n < 4:
        return lst[n]
    
    a, b, c, d = lst
    for _ in range(n - 3):
        a, b, c, d = b, c, d, 6 * d - 10 * c + 6 * b - a
    
    return d

