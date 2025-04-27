def is_valid_ipv4_address(address: str) -> bool:
    from re import compile, match

    # Regular expression to match a valid IPv4 address
    REGEX = compile(r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){4}$')

    # Check if the address matches the IPv4 pattern
    return bool(match(REGEX, address + '.'))

