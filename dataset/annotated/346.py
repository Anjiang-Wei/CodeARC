def calculate_rectangle_area(d: float, l: float) -> float:
    # Check if the diagonal is less than or equal to the side
    if d <= l:
        return "Not a rectangle"
    # Calculate the area using the formula and round to two decimal places
    return round(l * (d * d - l * l) ** 0.5, 2)

