def reverse_binary_and_convert_to_int(n: int) -> int:
    return int(bin(n)[:1:-1], 2)

