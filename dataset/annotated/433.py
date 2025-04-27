def is_triangular_number(t: int) -> bool:
    x = int((t * 2) ** 0.5)
    # Check if the number is a triangular number
    return t == x * (x + 1) // 2

