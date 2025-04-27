def solution(string):
    """
    :type string: str
    :rtype: str
    """
    # Split the string into words and filter based on the first character
    uppercase_words = [word for word in string.split() if word[0].isupper()]
    lowercase_words = [word for word in string.split() if word[0].islower()]
    
    # Concatenate uppercase and lowercase words maintaining their order
    return ' '.join(uppercase_words + lowercase_words)

