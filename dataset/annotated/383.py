def transform_digits(s: str) -> str:
    return s.translate(str.maketrans("1234567890", "9876043215"))

