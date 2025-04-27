def solution(name):
    import re
    # Convert the name to uppercase and find all valid characters
    return "".join(re.findall("[A-Z\s!]+", name.upper()))

