def solution(l):
    # Return a new list with the strings filtered out
    return [i for i in l if not isinstance(i, str)]

