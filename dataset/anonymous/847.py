def solution(a1, a2, a3):
    return [[x, y, x + y] for x in a1 for y in a2 if x + y in a3]

