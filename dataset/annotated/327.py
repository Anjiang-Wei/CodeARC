def transform_text(text: str, encryptKey: int, mode: str) -> str:
    """
    :type text: str
    :type encryptKey: int
    :type mode: str ('encrypt' or 'decrypt')
    :rtype: str
    """
    from collections import deque

    KEYBOARD = ['zxcvbnm,.', 'ZXCVBNM<>', 'asdfghjkl', 'ASDFGHJKL', 'qwertyuiop', 'QWERTYUIOP']
    
    def converter(text, encryptKey, sens):
        deques = list(map(deque, KEYBOARD))
        for i, deq in enumerate(deques):
            deq.rotate(-sens * (encryptKey // 10**(i//2) % 10))
        return text.translate(str.maketrans(''.join(KEYBOARD), ''.join(''.join(deq) for deq in deques)))
    
    if mode == 'encrypt':
        return converter(text, encryptKey, 1)
    elif mode == 'decrypt':
        return converter(text, encryptKey, -1)
    else:
        raise ValueError("Mode should be 'encrypt' or 'decrypt'")

