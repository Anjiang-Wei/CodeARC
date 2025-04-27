def encode_message(message: str) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode_message('test')
    'TGST'
    >>> encode_message('This is a message')
    'tHKS KS C MGSSCGG'
    """

    def switch_case(ch: str) -> str:
        if ord("A") <= ord(ch) <= ord("Z"):
            return chr(ord(ch) + 32)
        elif ord("a") <= ord(ch) <= ord("z"):
            return chr(ord(ch) - 32)
        else:
            return ch
    
    def vowel_change(ch: str) -> str:
        return ch if ch not in "aeiouAEIOU" else chr(ord(ch) + 2)
    
    m = "".join(map(switch_case, message))
    return "".join(map(vowel_change, m))

