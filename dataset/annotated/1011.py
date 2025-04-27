def add_numbers(a: float, b: float) -> float | None:
    try:
        return a + b
    except TypeError:
        return None

