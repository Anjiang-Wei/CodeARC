def is_valid_integer_string(text: str) -> bool:
    text = text.strip()
    if len(text) < 1:
        return None
    else:
        if text[0] in '+-':
            text = text[1:]
        return text.isdigit()

