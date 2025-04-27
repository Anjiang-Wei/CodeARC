def is_valid_bracket_sequence(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    bracket_map = {"]": "[", "}": "{", ")": "("}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or bracket_map[char] != stack.pop():
                return False
        else:
            return False
    return not stack

