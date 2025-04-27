def solution(packet):
    from string import ascii_uppercase

    # Create a dictionary with letter values
    values = {x: i for i, x in enumerate(ascii_uppercase, 1)}

    # Calculate the quicksum
    quicksum_value = sum(values.get(c, 0) * i for i, c in enumerate(packet, 1))

    # Check if all characters are either spaces or uppercase letters
    is_valid = all(c.isspace() or c.isupper() for c in packet)

    # Return the quicksum if valid, otherwise return 0
    return quicksum_value * is_valid

