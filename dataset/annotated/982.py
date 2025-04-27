def swap_first_letters_of_words(words: str) -> str:
    a, b = words.split()
    # Swap the first letters of the two words
    return '{}{} {}{}'.format(b[0], a[1:], a[0], b[1:])

