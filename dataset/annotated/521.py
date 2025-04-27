def find_odd_count_chars(s: str) -> list:
    from collections import Counter
    
    # Count characters in reverse order to prioritize last occurrences
    d = Counter(reversed(s))
    
    # Collect characters with odd counts and reverse the list to maintain order
    return [x for x in d if d[x] % 2][::-1]

