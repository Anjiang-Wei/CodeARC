def is_last_char_isolated_alpha(txt: str) -> bool:
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    is_last_char_isolated_alpha("apple pie") ➞ False
    is_last_char_isolated_alpha("apple pi e") ➞ True
    is_last_char_isolated_alpha("apple pi e ") ➞ False
    is_last_char_isolated_alpha("") ➞ False 
    '''

    if len(txt) == 0: return False
    if len(txt) == 1: return txt.isalpha()
    return txt[-1].isalpha() and txt[-2] == " "

