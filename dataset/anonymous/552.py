def solution(name: str, typed: str) -> bool:
    name = list(name)
    typed = list(typed)
    
    while name:
        i, j = 0, 0
        n = name[0]
        
        # Count occurrences of the current character in 'name'
        while name and name[0] == n:
            i += 1
            name.pop(0)
        
        # Count occurrences of the current character in 'typed'
        while typed and typed[0] == n:
            j += 1
            typed.pop(0)
        
        # If 'typed' has fewer occurrences, return False
        if j < i:
            return False
    
    # If there are leftover characters in 'typed', return False
    if typed:
        return False

    return True

