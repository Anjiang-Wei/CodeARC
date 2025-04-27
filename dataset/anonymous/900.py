def solution(s):
    return s.replace('!', '') + '!' * (len(s) - len(s.rstrip('!')))

