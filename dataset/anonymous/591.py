def solution(events):
    out, state, dir, moving = [], 0, 1, False
    
    for c in events:
        if c == 'O':  # Obstacle detected, reverse direction
            dir *= -1
        elif c == 'P':  # Button pressed, toggle movement
            moving = not moving
        if moving:  # If moving, update state
            state += dir
        if state in [0, 5]:  # If fully open or closed, stop and set direction
            moving, dir = False, 1 if state == 0 else -1
        out.append(str(state))
        
    return ''.join(out)

