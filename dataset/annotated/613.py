def has_triple_and_double_pattern(num1: int, num2: int) -> bool:
    return any(i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789')

