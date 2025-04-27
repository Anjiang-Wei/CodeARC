def solution(string):
    from collections import Counter
    
    # Count the occurrences of each character in the string
    cs = Counter(string)
    
    # Construct a new string with only characters that appear more than once
    return ''.join(c for c in string if cs[c] > 1)

