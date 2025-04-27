def solution(x, y):
    # Calculate the greatest common divisor using the Euclidean algorithm
    while y:
        x, y = y, x % y
    return x

