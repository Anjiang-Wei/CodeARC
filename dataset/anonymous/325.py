def solution(word):
    return ['{:08b}'.format(ord(c)) for c in word]

