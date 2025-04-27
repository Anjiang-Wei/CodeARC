def solution(word):
    import re
    
    # Define the pattern to find vowels not at the end of the word
    KA_PATTERN = re.compile(r'(?![aeiou]+$)([aeiou]+)', re.I)
    
    # Substitute the pattern with 'ka' after the vowels
    return 'ka' + KA_PATTERN.sub(r'\1ka', word)

