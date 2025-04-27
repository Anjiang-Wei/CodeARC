def calculate_slope(a: int, b: int, c: int, d: int) -> str:
    if c - a == 0:
        return "undefined"
    return str((d - b) // (c - a))

