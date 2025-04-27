def solution(n, m):
    from math import log2

    # Check if the interval contains a power of 2
    if int(log2(m)) > int(log2(n)):
        return 2**int(log2(m))

    # Adjust endpoints to exclude odd numbers
    n += n % 2
    m -= m % 2
    if n == m:
        return n

    # Recurse with halved endpoints and multiply the result by 2
    return 2 * solution(n // 2, m // 2)

