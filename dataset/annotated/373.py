def defang_ip_address(ip_address: str) -> str:
    return ip_address.replace('.', '[.]')

