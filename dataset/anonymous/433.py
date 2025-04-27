def solution(t):
    x = int((t * 2) ** 0.5)
    # Check if the number is a triangular number
    return t == x * (x + 1) // 2

