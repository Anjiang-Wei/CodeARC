def extrapolated_points_per_48(ppg: float, mpg: float) -> float:
    # Calculate extrapolated points per 48 minutes
    return round(48.0 / mpg * ppg, 1) if mpg > 0 else 0

