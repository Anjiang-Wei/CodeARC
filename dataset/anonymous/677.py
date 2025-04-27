def solution(n):
    from math import ceil, sqrt
    # Calculate the number of layers required to store up to n
    return ceil(sqrt(n)) // 2 + 1

