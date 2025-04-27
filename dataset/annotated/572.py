def perform_operation(l_st: list, s: str, operation: str) -> any:
    from functools import reduce
    from operator import mul

    # Determine which operation to perform
    if operation == 'multiplication':
        return reduce(mul, l_st)
    elif operation == 'addition':
        return sum(l_st)
    elif operation == 'reverse':
        return s[::-1]
    else:
        return None  # or raise an exception if an invalid operation is provided

