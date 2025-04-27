def solution(s):
    import string
    
    # Create translation table for shifting letters and wrapping Z to A
    translation_table = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'bcdEfghIjklmnOpqrstUvwxyzA'
    )
    
    # Convert string to lowercase and apply translation
    return s.lower().translate(translation_table)

