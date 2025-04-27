def solution(arr, n): 
    from functools import reduce
    return reduce(lambda x, y: x * y, arr) % n

