def extract_digits(input_string: str) -> str:
    return ''.join(filter(str.isdigit, input_string)) if isinstance(input_string, str) else 'Invalid input !'

