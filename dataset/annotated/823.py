def validate_message_format(msg: str) -> bool:
    import re
    # Validate the message format using regex
    return bool(re.match(r'^MDZHB \d\d \d\d\d [A-Z]+ \d\d \d\d \d\d \d\d$', msg))

