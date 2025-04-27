def polynomial_multiply(p1: list[int], p2: list[int]) -> list[int]:
    if not p1 or not p2:
        return []
    n = len(p1) + len(p2) - 1
    p = [0] * n
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            p[i + j] += a * b
    return p

