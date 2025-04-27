def is_valid_braces_sequence(s: str) -> bool:
    BRACES = {'(': ')', '[': ']', '{': '}'}
    
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack

