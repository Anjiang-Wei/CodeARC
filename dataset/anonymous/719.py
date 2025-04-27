def solution(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]

