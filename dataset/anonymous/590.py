def solution(arr):
    for x in arr:
        if type(x) != int:
            return False
    return '{0:b}'.format(sum(arr))

