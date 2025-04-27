def is_valid_parentheses_sequence(s: str) -> bool:
    brackets = {"}": "{", "]": "[", ")": "("}
    stack = []
    
    for c in s:
        if c in "[({":
            stack.append(c)
        elif c in "])}":
            if not stack or stack.pop() != brackets[c]:
                return False
    
    return not stack

