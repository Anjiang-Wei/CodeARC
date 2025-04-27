def solution(a, b):
    # XOR the numbers and count the number of 1s in the binary representation
    return bin(a ^ b).count('1')

