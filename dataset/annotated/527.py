def is_valid_triangle(side1: float, side2: float, side3: float) -> bool:
    # Check if the sum of any two sides is greater than the third side
    return (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2)

