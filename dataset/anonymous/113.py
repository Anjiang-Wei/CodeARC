def solution(arr):  
    return sum(x for x in arr[::2] if x % 2 == 0)

