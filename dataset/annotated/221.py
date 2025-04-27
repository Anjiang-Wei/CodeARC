from typing import List

def calculate_polynomial_derivative(coefficients: List[int]) -> List[int]:
    # Calculate the derivative of the polynomial
    return [i * x for i, x in enumerate(coefficients)][1:]

