def generate_linear_space(start: float, stop: float, number: int) -> list:
    from numpy import linspace
    return list(linspace(start, stop, number))

