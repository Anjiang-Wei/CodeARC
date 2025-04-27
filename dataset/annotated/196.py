def sum_of_odd_length_subarrays(arr: list[int]) -> int:
    sum_ = 0
    n = len(arr)
    for i in range(n):
        # arr[i] occurs (i + 1) * (n - i) times in all subarrays
        times = ((i + 1) * (n - i) + 1) // 2
        sum_ += arr[i] * times
    return sum_

