def solution(nums, n):
    nth_nums = list(map(lambda x: x ** n, nums))
    return nth_nums

