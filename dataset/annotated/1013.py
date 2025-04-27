def count_holes_in_number(n: int) -> int:
    # Dictionary to map digits to their respective "hole" counts
    hole_count = {'0': 1, '6': 1, '9': 1, '8': 2}
    
    # Convert the number to a string and sum the hole counts for each digit
    return sum(hole_count.get(d, 0) for d in str(n))

