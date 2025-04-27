def solution(a, b):
    from math import pi
    # Calculate area using the formula for the area of an ellipse
    area = pi * a * b
    # Calculate perimeter using the given approximation formula
    perimeter = pi * (1.5 * (a + b) - (a * b) ** 0.5)
    # Return formatted string with area and perimeter
    return f"Area: {area:.1f}, perimeter: {perimeter:.1f}"

