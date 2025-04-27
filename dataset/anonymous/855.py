def solution(N, x, y):
    # Check if the difference between y and x is even
    # or if any knight's n value is even
    return (y - x) % 2 == 0 or any(n % 2 == 0 for n in N)

