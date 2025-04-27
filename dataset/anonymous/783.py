def solution(mana):
    import re
    
    # Count occurrences of each mana type
    n = {c: mana.lower().count(c) for c in 'wubrg' if mana.lower().count(c) > 0}
    
    # Split the string to find generic mana
    m = re.split(r'\D', mana)
    
    # Check if the sum of all mana types matches the length of the input
    if sum(n.values()) + sum([len(c) for c in m]) != len(mana):
        return None
    
    # Calculate the total generic mana
    p = sum([int(c) for c in m if c != ''])
    
    # Add generic mana to the dictionary if greater than 0
    if p > 0:
        n['*'] = p
    
    return n

