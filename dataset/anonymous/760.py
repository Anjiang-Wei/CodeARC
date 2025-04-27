def solution(message):
    from string import ascii_lowercase as alphabet
    # Create a translation table to map each letter to its reverse counterpart
    translation_table = str.maketrans(alphabet, alphabet[::-1])
    # Translate the message using the translation table
    return message.translate(translation_table)

