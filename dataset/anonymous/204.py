def solution(n):
    if n < 0:
        return False
    return n**(1/2) == int(n**(1/2))

