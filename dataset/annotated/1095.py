def is_valid_braces_sequence(string: str) -> bool:
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    
    for character in string:
        if character in braces:
            stack.append(character)
        else:
            if not stack or braces[stack.pop()] != character:
                return False
    
    return not stack

