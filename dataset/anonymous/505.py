def solution(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return []

