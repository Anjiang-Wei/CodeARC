def xor_hex_strings(hex_str1: str, hex_str2: str) -> str:
    return "".join(f"{int(x, 16) ^ int(y, 16):x}" for x, y in zip(hex_str1, hex_str2))

