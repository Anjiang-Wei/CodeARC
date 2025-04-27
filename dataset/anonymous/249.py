def solution(a, b, margin=0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

