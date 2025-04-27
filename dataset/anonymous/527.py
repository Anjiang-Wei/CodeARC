def solution(a, b, c):
    # Check if the sum of any two sides is greater than the third side
    return (a < b + c) and (b < a + c) and (c < a + b)

