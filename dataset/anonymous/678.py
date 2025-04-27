def solution(a, b, c):
    # Calculate the perimeter
    p = a + b + c
    # Calculate the semi-perimeter
    ph = p / 2
    # Check if the area equals the perimeter
    return p * p == ph * (ph - a) * (ph - b) * (ph - c)

