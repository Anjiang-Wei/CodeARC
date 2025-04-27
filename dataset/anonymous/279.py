def solution(input):
    import re
    
    try:
        # Remove spaces and convert numbers to integers
        expression = re.sub(r'(\d+)', lambda m: str(int(m.group(1))), input.replace(" ", ""))
        # Evaluate the expression
        result = eval(expression)
        # Return as integer if possible, else as float
        return int(result) if result == int(result) else float(result)
    except:
        # Return False for any error
        return False

