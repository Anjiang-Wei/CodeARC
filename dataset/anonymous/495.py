def solution(s):
    from collections import Counter
    
    # Filter alphanumeric characters and convert to lowercase
    c = Counter(filter(str.isalnum, s.lower()))
    
    # Calculate the length of the longest palindrome
    # Sum of pairs (v//2*2) and add 1 if there's any odd count (v%2)
    return sum(v // 2 * 2 for v in c.values()) + any(v % 2 for v in c.values())

