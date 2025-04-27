def reverse_inner_chars_in_words(s: str) -> str:
    return ' '.join(w[-2::-1] + w[-1] for w in s.split())

