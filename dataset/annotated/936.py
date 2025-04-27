def hex_to_rgb(hex_string: str) -> dict[str, int]:
    # Convert the hexadecimal string to an RGB dictionary
    return {i: int(hex_string[j:j+2], 16) for i, j in zip('rgb', [1, 3, 5])}

