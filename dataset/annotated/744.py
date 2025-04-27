def encode_word_to_parentheses(word: str) -> str:
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

