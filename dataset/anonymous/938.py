def solution(words=""):
    if not isinstance(words, str):
        return {'vowels': 0, 'consonants': 0}
    
    # Filter only alphabetic characters and convert to lowercase
    letter = "".join([c.lower() for c in words if c.isalpha()])
    
    # Count vowels
    vowel = "".join([c for c in letter if c in 'aeiou'])
    
    # Count consonants
    consonant = "".join([c for c in letter if c not in 'aeiou'])
    
    return {'vowels': len(vowel), 'consonants': len(consonant)}

