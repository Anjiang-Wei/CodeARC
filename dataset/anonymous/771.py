def solution(sentence):
    # Reverse words with 5 or more letters
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

