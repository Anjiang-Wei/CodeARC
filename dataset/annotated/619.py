def sum_of_quadratic_roots(a: float, b: float, c: float) -> float | None:
    import math
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if roots are real
    if discriminant >= 0:
        # Calculate the roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        # Return the sum of the roots rounded to 2 decimal places
        return round(root1 + root2, 2)
    
    # Return None if no real roots
    return None

