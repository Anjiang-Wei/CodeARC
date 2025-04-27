def solution(string):
    import re
    # Check if the input is a valid string
    if not isinstance(string, str):
        return 'Please enter a valid string'
    # Use regex to find duplicates and format them with brackets
    return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string)

