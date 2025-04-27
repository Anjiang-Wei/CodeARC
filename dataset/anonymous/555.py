def solution(string):
    import re
    # Use regex to insert underscores before uppercase letters and convert to lowercase
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()

