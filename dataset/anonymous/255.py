def solution(yourID):
    import re
    # Check if the given string is a valid first name or hyphenated first name
    return bool(re.match(r'(-[A-Z][a-z]+)+$', '-' + yourID))

