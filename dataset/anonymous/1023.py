def solution(equation):
    import re
    
    # Remove all spaces from the equation
    equation = re.sub(r'\s+', '', equation)
    
    # Replace operators with their respective operations enclosed in parentheses
    equation = equation.replace('+', ')+')
    equation = equation.replace('-', ')-')
    equation = equation.replace('*', ')*')
    equation = equation.replace('/', ')//')
    equation = equation.replace('%', ')%')
    equation = equation.replace('^', ')**')
    
    # Add opening parentheses to the start of the equation
    equation = '(' * equation.count(')') + equation
    
    try:
        # Evaluate the equation
        return eval(equation)
    except ZeroDivisionError:
        # Return None if there is a division or modulo by zero
        return None
    except:
        # Return None for any other exceptions
        return None

