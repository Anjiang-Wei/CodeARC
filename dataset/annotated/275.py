def calculate_sorted_pairs(a: int, b: int, c: int, d: int) -> list[list[int]]:
    # Calculate possible pairs (e, f) using given formulas
    e = sorted([abs(a * d - b * c), abs(a * c + b * d)])
    f = sorted([abs(a * c - b * d), abs(a * d + b * c)])
    
    # If both pairs are the same, return one of them
    if e == f:
        return [e]
    else:
        # Return both pairs sorted by the first element of each pair
        return sorted([e, f])

