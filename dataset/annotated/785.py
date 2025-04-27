def hex_string_sum(s: str) -> int:
    # Translate 'O' to '0' and 'S' to '5', then split the string into words
    translated_words = s.translate(str.maketrans('OS', '05')).split()
    
    # Calculate the sum of valid hex values
    hex_sum = sum(int(w, 16) for w in translated_words if set(w) <= set('0123456789ABCDEF'))
    
    return hex_sum

