def solution(sentence, fairy):
    from collections import Counter
    
    c = Counter(sentence)
    d = {'good': ['ruby', 'crystal'], 'evil': ['python', 'squirrel']}
    
    # Calculate the count based on the fairy type
    return {s: c[s[0]] + 2 * c[s[0].upper()] for s in d[fairy]}

