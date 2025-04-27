def calculate_interests(principal: float, interest: float, periods: int) -> list[int]:
    # Calculate simple interest
    simple_interest = principal * (1 + interest * periods)
    
    # Calculate compound interest
    compound_interest = principal * (1 + interest) ** periods
    
    # Return both results rounded to the nearest integer
    return [round(simple_interest), round(compound_interest)]

