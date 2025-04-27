def solution(vals):
    a = b = 0
    for n in vals:
        a, b = b, max(a + n, b)
    return max(a, b)

