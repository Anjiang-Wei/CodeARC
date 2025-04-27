def solution(n, k):
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
    return v + 1

