def solution(arr):
    sum_ = 0
    n = len(arr)
    for i in range(n):
        # arr[i] occurs (i + 1) * (n - i) times in all subarrays
        times = ((i + 1) * (n - i) + 1) // 2
        sum_ += arr[i] * times
    return sum_

