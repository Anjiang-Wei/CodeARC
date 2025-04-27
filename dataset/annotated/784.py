def capitalize_words_longer_than_two(str_: str) -> str:
    return ' '.join(w.capitalize() if len(w) > 2 else w for w in str_.split(' '))

