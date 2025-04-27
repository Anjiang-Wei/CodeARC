def solution(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        # Calculate the interest for the year, subtract the tax, and add to principal
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years

