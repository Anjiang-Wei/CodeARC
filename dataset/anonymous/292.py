def solution(n):
    from functools import reduce
    from operator import mul
    
    s = str(n)
    # Iterate over all possible splits and calculate the product
    return max(
        reduce(mul, map(int, (s[:i], s[i:j], s[j:])))
        for i in range(1, len(s) - 1)
        for j in range(i + 1, len(s))
    )

