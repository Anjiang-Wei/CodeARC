def solution(word):
    return [i for i, x in enumerate(word, 1) if x.lower() in 'aeiouy']

