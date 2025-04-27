def substitute_message(message: str, key: str) -> str:
    # Create a case-sensitive substitution dictionary
    key = key.lower() + key.upper()
    substitution_dict = {char: key[i-1] if i % 2 else key[i+1] for i, char in enumerate(key)}
    
    # Substitute each character in the message using the dictionary
    return ''.join(substitution_dict.get(char, char) for char in message)

