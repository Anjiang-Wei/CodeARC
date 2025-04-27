def solution(a, b):
    """
    :type a: int or float
    :type b: int or float
    :rtype: dict
    """
    # Define all operations as lambda functions
    add = lambda a, b: a + b
    multiply = lambda a, b: a * b
    divide = lambda a, b: a / b
    mod = lambda a, b: a % b
    exponent = lambda a, b: a ** b
    subt = lambda a, b: a - b

    # Return a dictionary with all results
    return {
        'addition': add(a, b),
        'multiplication': multiply(a, b),
        'division': divide(a, b),
        'modulus': mod(a, b),
        'exponential': exponent(a, b),
        'subtraction': subt(a, b)
    }

