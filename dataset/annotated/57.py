def find_closest_vowel_between_consonants(word: str) -> str:
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    find_closest_vowel_between_consonants("yogurt") ==> "u"
    find_closest_vowel_between_consonants("FULL") ==> "U"
    find_closest_vowel_between_consonants("quick") ==> ""
    find_closest_vowel_between_consonants("ab") ==> ""
    """

    def is_vowel(ch: str) -> bool:
        return ch in "aeiouAEIOU"

    for i in range(len(word) - 2, 0, -1):
        if is_vowel(word[i]) and not is_vowel(word[i-1]) and not is_vowel(word[i+1]):
            return word[i]
    return ""

