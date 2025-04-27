def solution(s, n):
    # Split the string into a list of words
    words = s.split(', ')
    
    # Sort the words based on the nth character, case-insensitive
    sorted_words = sorted(words, key=lambda word: word[n-1].lower())
    
    # Join the sorted words back into a string
    return ', '.join(sorted_words)

