def solution(a):
    return all(a[i] + a[-i-1] <= 10 for i in range(len(a) // 2))

