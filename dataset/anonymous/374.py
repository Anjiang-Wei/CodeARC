def solution(s):
    from collections import Counter
    
    # Count the frequency of each character
    char_count = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # A string can be rearranged to form a palindrome if at most one character has an odd frequency
    return odd_count < 2

