def solution(s):
    if not s:
        return s
    
    swap = [False]
    
    # Iterate over each character in the string
    result = ''.join(
        c.swapcase() if swap[0] else c  # Swap case if CapsLock is enabled
        for c in s
        if c not in "aA" or swap.__setitem__(0, not swap[0])  # Toggle CapsLock on 'A' or 'a'
    )
    
    return result

