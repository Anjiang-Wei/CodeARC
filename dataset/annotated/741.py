def binary_operation(n1: str, n2: str, o: str) -> str:
    operators = {
        "add": (lambda x, y: x + y),
        "subtract": (lambda x, y: x - y),
        "multiply": (lambda x, y: x * y),
    }
    
    # Convert binary strings to integers, perform the operation, and convert back to binary string
    return "{:b}".format(operators[o](int(n1, 2), int(n2, 2)))

