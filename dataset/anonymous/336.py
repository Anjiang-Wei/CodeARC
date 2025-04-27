def solution(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0

