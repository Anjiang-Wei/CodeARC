def calculate_polygon_area_in_circle(circle_radius: float, number_of_sides: int) -> float:
    from math import sin, pi
    # Calculate the area using the formula for a regular polygon inside a circumcircle
    area = 0.5 * number_of_sides * circle_radius ** 2 * sin(2 * pi / number_of_sides)
    # Return the area rounded to 3 decimal places
    return round(area, 3)

