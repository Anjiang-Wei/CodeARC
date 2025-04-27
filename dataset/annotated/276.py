def insert_dash_between_uppercase(s: str) -> str:
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

