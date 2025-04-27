def solution(test_key):
    from collections import Counter
    from string import ascii_lowercase
    
    cnt = Counter(test_key)
    # Create a string by iterating over each letter in the alphabet
    # and getting its count from the counter, defaulting to 0 if not present
    return ''.join(str(cnt.get(a, 0)) for a in ascii_lowercase)

