def frequency_sort(s: str) -> str:
    from collections import Counter
    
    # Count the frequency of each character in the string
    count = Counter(s)
    
    # Sort the string based on the frequency of each character
    # Characters with the same frequency maintain their original order
    return ''.join(sorted(s, key=lambda c: -count[c]))

