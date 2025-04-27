def calculate_bitwise_complement(N: int) -> int:
    # Calculate the bitwise complement by shifting 1 left by the length of the binary representation of N minus 2 (to exclude '0b')
    # Subtract N and 1 to get the complement
    return (1 << (len(bin(N)) - 2)) - N - 1

