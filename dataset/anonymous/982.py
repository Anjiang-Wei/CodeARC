def solution(words):
    a, b = words.split()
    # Swap the first letters of the two words
    return '{}{} {}{}'.format(b[0], a[1:], a[0], b[1:])

