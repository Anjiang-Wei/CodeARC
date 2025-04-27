def solution(lst, key=0):
    from itertools import groupby
    # Group the list based on whether elements are less than the key
    return [list(g) for _, g in groupby(lst, lambda a: a < key)]

