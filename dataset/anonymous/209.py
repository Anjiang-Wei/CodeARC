def solution(s):
    # Count the number of 'r' characters in the string
    red_plate_count = s.count("r")
    
    # Calculate the total cost considering every 5th plate is free
    total_cost = 2 * (red_plate_count - red_plate_count // 5)
    
    return total_cost

