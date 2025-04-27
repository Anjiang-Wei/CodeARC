def solution(arr, k):
    arr = sorted(arr)
    s = 0
    for i, v in enumerate(arr):
        s += v
        if s >= k:
            return i

