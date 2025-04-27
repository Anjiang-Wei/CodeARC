def solution(string):
    # Check if the string is empty, return None if true
    if len(string) == 0:
        return None
    
    # Create a dictionary with characters as keys and their ASCII values as values
    # Only include alphabetic characters and ignore duplicates
    return {c: ord(c) for c in set(string) if c.isalpha()}

