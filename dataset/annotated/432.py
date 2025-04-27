def calculate_draw_probability(balls: list, sequence: list, is_replaced: bool) -> float:
    from collections import Counter
    
    # Count the occurrences of each color in the bag
    color_count = Counter(balls)
    total_balls = len(balls)
    probability = 1
    
    for color in sequence:
        # Calculate the probability of drawing the current color
        probability *= color_count.get(color, 0) / total_balls
        
        # If the ball is not replaced, adjust the counts
        if not is_replaced:
            total_balls -= 1
            color_count[color] -= 1
    
    # Return the probability rounded to 3 decimal places
    return round(probability, 3)

