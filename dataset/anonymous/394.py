def solution(str_):
    if not str_:
        return []

    def prefix2(a, b, num):
        for i in range(num, -1, -1):
            if b.startswith(a[:i]):
                return i

    z = []
    k = len(str_)
    for i in range(len(str_)):
        z.append(prefix2(str_[i:], str_[:k - i], k - i))
    
    return z

