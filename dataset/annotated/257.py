def convert_twos_complement(binary: str = None, bits: int = None, n: int = None, mode: str = 'to_twos_complement') -> int | str:
    """
    :param binary: str, binary string with spaces (e.g., "0000 0001")
    :param bits: int, number of bits
    :param n: int, integer to convert to binary
    :param mode: str, 'to_twos_complement' or 'from_twos_complement'
    :rtype: int or str
    """
    def to_twos_complement(binary: str, bits: int) -> int:
        # Convert binary string to integer considering two's complement
        return int(binary.replace(' ', ''), 2) - 2 ** bits * int(binary[0])

    def from_twos_complement(n: int, bits: int) -> str:
        # Convert integer to binary string with specified bits
        return '{:0{}b}'.format(n & 2 ** bits - 1, bits)

    if mode == 'to_twos_complement' and binary is not None and bits is not None:
        return to_twos_complement(binary, bits)
    elif mode == 'from_twos_complement' and n is not None and bits is not None:
        return from_twos_complement(n, bits)
    else:
        raise ValueError("Invalid parameters or mode")

