def solution(x):
    # Check if x is not zero and x is a power of two using bitwise operation
    return x != 0 and ((x & (x - 1)) == 0)

