def solution(a, b, c, d):
    if c - a == 0:
        return "undefined"
    return str((d - b) // (c - a))

