def solution(n, m):
    from math import gcd
    # Calculate the number of black cells using the formula
    return (n + m) - 2 + gcd(n, m)

