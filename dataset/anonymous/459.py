def solution(lst, n):
    return sum(x**n - x for x in lst)

