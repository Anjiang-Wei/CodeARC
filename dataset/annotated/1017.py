def flip_binary_string(binary_string: str) -> str:
    return binary_string.translate(str.maketrans("01", "10"))

