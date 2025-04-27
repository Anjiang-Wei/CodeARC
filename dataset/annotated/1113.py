def find_vowel_positions(word: str) -> list[int]:
    return [i for i, x in enumerate(word, 1) if x.lower() in 'aeiouy']

