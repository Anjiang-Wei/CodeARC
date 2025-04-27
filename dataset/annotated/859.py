def convert_to_mid_endian_hex(n: int) -> str:
    import re
    h = hex(n)[2:].upper()
    r = re.findall('..', '0' * (len(h) % 2) + h)
    # Rearrange the bytes to mid-endian format
    return "".join(r[1::2][::-1] + r[0::2])

