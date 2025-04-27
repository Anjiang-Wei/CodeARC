def solution(arr):
    while len(arr) > 1:
        arr = [x + y for x, y in zip(arr, arr[1:])]
    return arr[0]

