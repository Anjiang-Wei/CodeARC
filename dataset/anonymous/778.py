def solution(data):
    from collections import Counter
    
    cnts = Counter(data)
    mx, mn = max(cnts.values()), min(cnts.values())
    
    # Return sorted list of elements with maximum frequency, excluding those with minimum frequency
    return sorted([k for k in cnts if cnts[k] == mx and cnts[k] != mn])

