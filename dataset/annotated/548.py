def evaluate_expression(st: str) -> str:
    import re
    
    # Remove all characters except digits, operators, and decimal points
    st = re.sub(r'[^-+*/\d.]', '', st)
    
    # Evaluate the expression
    result = eval(st)
    
    # Round the result to the nearest integer and convert to string
    return str(int(round(result)))

