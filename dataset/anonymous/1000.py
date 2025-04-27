def solution(s, i):
    # Check if the index is within the valid range and if the character at the index is a vowel
    return 0 <= i < len(s) and s[i] in "aieouAEIOU"

