def decompose_number_into_powers(n: int) -> list[list[int], int]:
    from math import log

    i = 2
    result = []
    while n >= i * i:
        k = int(log(n, i))
        result.append(k)
        n -= i ** k
        i += 1
    return [result, n]

