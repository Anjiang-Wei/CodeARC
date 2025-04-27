def solution(s: str) -> str:
    stack = []
    
    for char in s:
        # Check if the stack is not empty and the current character and the last character in the stack are the same letter in different cases
        if stack and char.lower() == stack[-1].lower() and char != stack[-1]:
            stack.pop()  # Remove the last character from the stack
        else:
            stack.append(char)  # Add the current character to the stack
    
    return ''.join(stack)  # Return the resulting good string

