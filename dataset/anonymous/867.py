def solution(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 += p0 * percent / 100.0 + aug
        year += 1
    return year

