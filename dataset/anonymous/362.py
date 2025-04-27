def solution(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))

