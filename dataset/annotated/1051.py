def insert_space_before_uppercase(s: str) -> str:
    return ''.join(' ' + c if c.isupper() else c for c in s)

