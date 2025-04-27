def solution(circle_radius, number_of_sides):
    from math import sin, pi
    # Calculate the area using the formula for a regular polygon inside a circumcircle
    area = 0.5 * number_of_sides * circle_radius ** 2 * sin(2 * pi / number_of_sides)
    # Return the area rounded to 3 decimal places
    return round(area, 3)

