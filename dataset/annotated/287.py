def digit_root_via_binary_ones(n: int) -> int:
    while n > 9:
        n = bin(n).count("1")
    return n

