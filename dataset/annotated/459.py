def calculate_polynomial_sum(lst: list, n: int) -> int:
    return sum(x**n - x for x in lst)

