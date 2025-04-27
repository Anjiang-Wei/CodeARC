def solution(n):
    from math import log10
    # Calculate the total cost of labels needed for enumeration
    return (n + 1) * int(log10(n) + 1) - (10 ** int(log10(n) + 1) - 1) // 9

