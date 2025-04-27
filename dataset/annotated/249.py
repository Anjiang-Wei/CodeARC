def compare_with_margin(a: float, b: float, margin: float = 0) -> int:
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

