def solution(radius):
    from math import pi
    # Check if the radius is a positive number
    if isinstance(radius, (int, float)) and radius > 0:
        # Calculate and return the area rounded to two decimal places
        return round(pi * radius ** 2, 2)
    else:
        # Return False if the radius is not valid
        return False

