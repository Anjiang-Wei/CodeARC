def solution(code):
    import re
    # Use regex to match the pattern described in the problem
    pattern = r'(?:[A-Z]\d){5}\.-[A-Z]%\d\.\d{2}\.'
    # Return True if the pattern is found, otherwise False
    return bool(re.search(pattern, code))

