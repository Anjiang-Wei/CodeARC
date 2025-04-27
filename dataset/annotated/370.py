def reverse_within_parentheses(s: str) -> str:
    stack = []
    for i in s:
        stack.append(i)
        
        if i == ')':
            # Find the position of the matching opening parenthesis
            opening = len(stack) - stack[::-1].index('(') - 1
            # Reverse the content inside the parentheses and switch directions
            stack = stack[:opening] + list(''.join(stack[opening+1:-1])[::-1])
            # Remove the original content inside the parentheses
            del stack[opening+1:]
    
    # Join the stack to form the final string
    return ''.join(stack)

