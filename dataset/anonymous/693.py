def solution(seq):
    return len({a - b for a, b in zip(seq, seq[1:])}) == 1

