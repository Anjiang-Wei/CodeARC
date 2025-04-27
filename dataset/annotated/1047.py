def generate_arithmetic_sequence(start: int, difference: int, count: int) -> str:
    return ', '.join(str(start + b * difference) for b in range(count))

