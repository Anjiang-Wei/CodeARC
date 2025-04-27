def insert_underscores(name: str) -> str:
    import re
    # Use regex to insert underscores before capital letters and numbers
    return re.sub(r"(?<=[^_-])_?(?=[A-Z])|(?<=[^\d_])_?(?=\d)", "_", name)

