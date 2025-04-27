def transform_word_to_phone_style(word: str) -> str:
    return word.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa'))

