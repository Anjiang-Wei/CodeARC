def replace_polish_characters(s: str) -> str:
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

