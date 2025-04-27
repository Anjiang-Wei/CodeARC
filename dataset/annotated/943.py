def count_differing_bits(a: int, b: int) -> int:
    # XOR the numbers and count the number of 1s in the binary representation
    return bin(a ^ b).count('1')

