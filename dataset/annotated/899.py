def is_valid_identifier(idn: str) -> bool:
    import re
    # Check if the identifier matches the pattern for a valid identifier
    return re.compile('^[a-z_\$][a-z0-9_\$]*$', re.IGNORECASE).match(idn) is not None

