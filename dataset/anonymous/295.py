def solution(arr):
    return sum(x**2 if i % 2 == 1 else x for i, x in enumerate(arr))

