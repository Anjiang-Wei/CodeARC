def count_set_bits_in_integer(n: int) -> int:
    return bin(n)[2:].count('1')

