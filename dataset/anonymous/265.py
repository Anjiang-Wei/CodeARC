def solution(s: str) -> str:
    if len(s) == 0:
        return s
    
    # Initialize a list with a placeholder at the start and end
    string = ['#']
    string.extend(list(s))
    string.append('#')
    
    # Iterate through the string to replace '?'
    for i in range(1, len(string) - 1):
        if string[i] == '?':
            # Try replacing '?' with a character that doesn't match neighbors
            for j in range(97, 123):  # ASCII values for 'a' to 'z'
                if string[i - 1] != chr(j) and string[i + 1] != chr(j):
                    string[i] = chr(j)
                    break
    
    # Join the list into a string, excluding the placeholders
    return ''.join(string[1:-1])

