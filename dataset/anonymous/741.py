def solution(n1, n2, o):
    operators = {
        "add": (lambda x, y: x + y),
        "subtract": (lambda x, y: x - y),
        "multiply": (lambda x, y: x * y),
    }
    
    # Convert binary strings to integers, perform the operation, and convert back to binary string
    return "{:b}".format(operators[o](int(n1, 2), int(n2, 2)))

