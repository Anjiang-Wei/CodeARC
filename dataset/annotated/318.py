def has_only_double_g(s: str) -> bool:
    import re
    # Check for any 'g' that is not immediately followed or preceded by another 'g'
    return not re.search(r'(?<!g)g(?!g)', s)

