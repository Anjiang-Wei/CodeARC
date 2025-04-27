def solution(code, chars="abcdefghijklmnopqrstuvwxyz"):
    import string
    
    # Convert the input code to lowercase
    code = code.lower()
    
    # Create a translation table for mirroring the specified characters
    translation_table = str.maketrans(chars, chars[::-1])
    
    # Translate the code using the translation table
    return code.translate(translation_table)

