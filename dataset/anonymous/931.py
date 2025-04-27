def solution(ppg, mpg):
    # Calculate extrapolated points per 48 minutes
    return round(48.0 / mpg * ppg, 1) if mpg > 0 else 0

