def is_valid_username(username: str) -> bool:
    import re
    # Check if the username matches the regex pattern for valid usernames
    return re.match('^[a-z0-9_]{4,16}$', username) is not None

