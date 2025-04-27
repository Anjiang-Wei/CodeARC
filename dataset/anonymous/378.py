def solution(n, r, c, candy):
    if candy > n:
        return [-1, -1, -1]
    
    # Calculate linear index in the current box
    linIdx = r * c - ((candy - 1) % (r * c) + 1)
    
    # Calculate box number, row, and column
    box_number = (candy - 1) // (r * c) + 1
    row = linIdx // c
    column = linIdx % c
    
    return [box_number, row, column]

