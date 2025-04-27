def solution(n):
    from math import log

    i = 2
    result = []
    while n >= i * i:
        k = int(log(n, i))
        result.append(k)
        n -= i ** k
        i += 1
    return [result, n]

