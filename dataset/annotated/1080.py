def is_balanced_brackets(s: str, caps: str) -> bool:
    stack = []
    openers, closers = caps[::2], caps[1::2]
    
    for char in s:
        if char in openers:
            # Check if the character is both an opener and closer
            if char in closers and stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        elif char in closers:
            # Check if the stack is empty or the last opener doesn't match
            if not stack or openers[closers.index(char)] != stack[-1]:
                return False
            else:
                stack.pop()
    
    # Return True if stack is empty, meaning all openers are closed
    return not stack

