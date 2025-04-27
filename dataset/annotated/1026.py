def determine_medal(string: str) -> str:
    # Count the rings in each letter
    ring_count = sum(map("abdegopqABBDOPQR".count, string))
    
    # Calculate the score by dividing the total number of rings by 2
    score = ring_count // 2
    
    # Determine the medal based on the score
    medals = ['Not even a medal!', 'Not even a medal!', 'Bronze!', 'Silver!', 'Gold!']
    
    # Return the appropriate medal
    return medals[min(4, score)]

