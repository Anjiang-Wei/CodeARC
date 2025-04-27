def solution(x):
    """
    :type x: int
    :rtype: int
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

