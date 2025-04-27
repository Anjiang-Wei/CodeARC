def solution(l): 
    return sorted(l) == list(range(min(l), max(l) + 1))

