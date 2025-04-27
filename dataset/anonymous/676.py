def solution(arr, n):
    if arr.count(n) != 2:
        return 0
    a = arr.index(n)
    b = arr.index(n, a + 1)
    return b - a + 1

