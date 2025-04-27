def sort_sentence_by_number(sentence: str) -> str:
    import re
    # Split the sentence into words and sort them based on the embedded number
    return " ".join(sorted(sentence.split(), key=lambda x: int(re.search(r'\d', x).group())))

