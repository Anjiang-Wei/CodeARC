def calculate_group_size(start_size: int, day: int) -> int:
    from math import floor
    # Calculate the group size on the 'day'-th day
    return floor((2 * day + start_size * (start_size - 1)) ** 0.5 + 0.5)

