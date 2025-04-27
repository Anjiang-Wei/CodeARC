def rotate_vowels_in_text(text: str, n: int) -> str:
    import re
    from collections import deque
    
    if text is None or text == "":
        return text
    
    tokens = re.split(r'([aeiouAEIOU])', text)
    if len(tokens) > 1:
        vowels = deque(tokens[1::2])
        vowels.rotate(n)
        tokens[1::2] = vowels
    
    return ''.join(tokens)

