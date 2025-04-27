from bisect import bisect_right

def solution(a, x):
    return bisect_right(a, x)

