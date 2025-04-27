def word_to_binary_strings(word: str) -> list[str]:
    return ['{:08b}'.format(ord(c)) for c in word]

