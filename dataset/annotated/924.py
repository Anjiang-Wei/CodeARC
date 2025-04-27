def calculate_total_circle_area(*diameters: float) -> str:
    import math
    # Calculate the total area of all circles
    total_area = round(sum([math.pi * (d**2) / 4 for d in diameters]))
    # Return the result in the specified format
    return 'We have this much circle: {}'.format(int(total_area))

