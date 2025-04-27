def has_uniform_letter_count(word: str) -> bool:
    from collections import Counter
    import re

    if type(word) is not str or not word:
        return False
    
    # Remove non-letter characters and convert to lowercase
    cleaned_word = re.sub(r'[^a-z]', "", word.lower())
    
    # Count occurrences of each letter
    letter_counts = Counter(cleaned_word)
    
    # Check if all counts are the same
    return len(set(letter_counts.values())) == 1

