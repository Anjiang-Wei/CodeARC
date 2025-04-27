def is_valid_mac_address(inputString: str) -> bool:
    import re
    # Check if the inputString matches the MAC-48 address pattern
    return bool(re.match("^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$", inputString.upper()))

