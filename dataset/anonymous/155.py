def solution(list_data):
    from functools import reduce
    return reduce(lambda x, y: x*y, set(list_data))

