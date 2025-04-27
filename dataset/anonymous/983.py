def solution(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            return i
    return -1

