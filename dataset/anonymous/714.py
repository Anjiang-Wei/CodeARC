def solution(s, c):
    if not s or not c:
        return []

    indexes = [i for i, ch in enumerate(s) if ch == c]
    if not indexes:
        return []
        
    return [min(abs(i - ic) for ic in indexes) for i in range(len(s))]

