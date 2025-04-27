def solution(numerator, denominator):
    import re
    # Calculate the division and split into integer and decimal parts
    integer_part, decimal_part = str(numerator * 1.0 / denominator).split('.')
    # Use regex to find repeating sequences and replace them with parentheses
    formatted_decimal = re.sub(r'([0-9])\1+', r'(\1)', decimal_part)
    # Return the formatted result
    return integer_part + '.' + formatted_decimal

