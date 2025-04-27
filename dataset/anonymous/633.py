def solution(s1, s2):
    from collections import Counter
    
    # Calculate the difference in character counts between s2 and s1
    # and return the character that appears three more times in s2.
    return next((Counter(s2) - Counter(s1)).elements())

