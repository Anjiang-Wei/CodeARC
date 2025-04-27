def calculate_years_to_reach_goal(principal: float, interest: float, tax: float, desired: float) -> int:
    years = 0
    
    while principal < desired:
        # Calculate the interest for the year, subtract the tax, and add to principal
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years

