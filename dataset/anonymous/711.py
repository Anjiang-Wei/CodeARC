def solution(sequence):
    for j, x in enumerate(sequence):
        i = sequence.index(x)
        if 0 <= i < j:
            return [i, j - i]
    return []

