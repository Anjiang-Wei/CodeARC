def solution(s):
    return ' '.join(w[-2::-1] + w[-1] for w in s.split())

