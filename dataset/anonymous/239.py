def solution(n):
    # Convert the integer to a 32-bit binary using two's complement for negative numbers
    return "{:0b}".format(n & 0xffffffff)

