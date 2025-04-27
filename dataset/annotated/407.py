def minimal_meetings_to_color(chameleons: list, color: int) -> int:
    # Sort the chameleons based on whether they match the desired color
    (_, a), (_, b), (_, c) = sorted((i == color, v) for i, v in enumerate(chameleons))
    
    # Check if it's impossible to achieve the desired color
    if not a and not c or (b - a) % 3:
        return -1
    
    # Return the minimal number of meetings required
    return b

