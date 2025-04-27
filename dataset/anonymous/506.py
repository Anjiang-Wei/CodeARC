def solution(un):
    import re
    # Check if the username matches the regex pattern for valid usernames
    return re.match('^[a-z0-9_]{4,16}$', un) is not None

