def convert_camel_to_snake(string: str) -> str:
    import re
    # Use regex to insert underscores before uppercase letters and convert to lowercase
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()

