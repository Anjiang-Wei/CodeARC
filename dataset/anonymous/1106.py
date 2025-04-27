def solution(a0):
    from itertools import count

    def repeat_sequence_len(n):
        memo = {}
        for i in count():
            if n in memo:
                return i - memo[n]
            memo[n] = i
            n = sum(d * d for d in map(int, str(n)))

    return repeat_sequence_len(a0)

