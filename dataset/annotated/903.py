def count_valleys(steps: str) -> int:
    level = 0
    in_valley = False
    count = 0
    
    for c in steps:
        if c == 'U':
            level += 1
        elif c == 'D':
            level -= 1
        
        # Check if we have exited a valley
        if level >= 0 and in_valley:
            count += 1
        
        # Update in_valley status
        in_valley = level < 0
    
    return count

