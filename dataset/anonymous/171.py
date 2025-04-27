def adjac(ele, sub=[]):
    if not ele:
        yield sub
    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                    for idx in adjac(ele[1:], sub + [j])]

def solution(test_tup):
    return list(adjac(test_tup))

