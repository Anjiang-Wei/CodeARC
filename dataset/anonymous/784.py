def solution(str_):
    return ' '.join(w.capitalize() if len(w) > 2 else w for w in str_.split(' '))

