def count_trailing_zeros_in_binary(n: int) -> int:
    res = 0
    while not n & 1:
        res += 1
        n >>= 1
    return res

