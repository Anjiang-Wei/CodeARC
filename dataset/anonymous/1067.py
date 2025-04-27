def solution(sequence):
    # Calculate the common ratio
    r = sequence[1] / sequence[0]
    
    # Check if the common ratio is within the valid range
    if abs(r) < 1:
        # Calculate the sum to infinity and round to 3 decimal places
        return round(sequence[0] / (1 - r), 3)
    else:
        # Return "No Solutions" if the common ratio is out of bounds
        return "No Solutions"

