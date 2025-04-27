from math import atan2, degrees

def calculate_dartboard_score(x: float, y: float) -> str:
    # Calculate the distance from the center and the angle
    r = (x*x + y*y)**0.5
    a = degrees(atan2(y, x)) + 9
    
    # Adjust angle to be positive
    a = a + 360 if a < 0 else a
    
    # Determine the sector number
    t = str([6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10][int(a) // 18])
    
    # Determine the score based on the distance
    for l, s in [(6.35, 'DB'), (15.9, 'SB'), (99, t), (107, 'T' + t), (162, t), (170, 'D' + t)]:
        if r <= l:
            return s
    
    # If outside all defined areas, return 'X'
    return 'X'

