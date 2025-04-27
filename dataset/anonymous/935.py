def solution(n, sequence):
    return sum(a == b for a, b in zip(sequence, sequence[n:]))

