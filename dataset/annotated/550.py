def sort_letters_preserve_others(s: str) -> str:
    a = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    return ''.join(next(a) if c.isalpha() else c for c in s)

