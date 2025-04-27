def is_non_divisible_after_reduction(n: int) -> bool:
    k = 2
    while n >= k and n % k:
        n -= n // k
        k += 1
    return n % k > 0

