def count_and_replace_odd_sequences(s: str) -> int:
    import re
    
    # Compile the pattern to find "odd" sequences
    pattern = re.compile('o(.*?)d(.*?)d')
    
    n = 0
    # Search and replace "odd" sequences until none are left
    while pattern.search(s):
        n += 1
        # Replace the found "odd" with the characters in between
        s = pattern.sub(r'\1\2', s, count=1)
    return n

