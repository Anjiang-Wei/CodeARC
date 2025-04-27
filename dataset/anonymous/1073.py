def solution(a, b):
    if not (a and b):
        return [a, b]
    if a >= 2 * b:
        return solution(a % (2 * b), b)
    if b >= 2 * a:
        return solution(a, b % (2 * a))
    return [a, b]

