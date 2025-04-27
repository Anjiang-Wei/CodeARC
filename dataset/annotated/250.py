def int_to_ip_address(int32: int) -> str:
    from ipaddress import IPv4Address
    return str(IPv4Address(int32))

