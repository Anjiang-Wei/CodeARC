def count_one_bits(x: int) -> int:
    """
    Counts the number of '1' bits in the binary representation of an integer.
    
    :param x: The integer to evaluate.
    :return: The count of '1' bits in the binary representation of x.
    """
    # Initialize count of '1' bits
    count = 0
    # Loop until x becomes zero
    while x:
        # Increment count if the last bit is '1'
        count += x & 1
        # Right shift x by 1 to check the next bit
        x >>= 1
    return count

