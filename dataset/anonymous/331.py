def solution(arr):
    return sum(arr) % len(arr) == 0 and sum(arr) > 0

