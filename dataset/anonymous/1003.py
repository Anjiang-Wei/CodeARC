def solution(word):
    """
    :type word: str
    :rtype: bool
    """
    # Check if the word is empty
    if len(word) == 0:
        return True
    # Check if all letters are uppercase or all are lowercase
    elif word.isupper() or word.islower():
        return True
    # Check if only the first letter is uppercase
    elif len(word) > 1:
        return word.istitle()
    else:
        return False

