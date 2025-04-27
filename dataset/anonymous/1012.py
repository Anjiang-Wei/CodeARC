def solution(arr):
    sum = max_sum = 0
    for n in arr:
        sum = max(sum + n, 0)
        max_sum = max(sum, max_sum)
    return max_sum

