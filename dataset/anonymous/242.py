def solution(a, b, n):
    remainder = int((a / b + 0.05) * 10) % 10
    # Check if the remainder is greater than 0 and is a multiple of n
    return remainder > 0 and remainder % n == 0

