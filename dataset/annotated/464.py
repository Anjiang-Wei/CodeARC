def sum_of_cycles(n: int, m: int) -> float:
    # Calculate the number of complete cycles and the remainder
    re, c = divmod(n, m)
    
    # Sum of a complete cycle (0 to m-1) is m*(m-1)/2
    # Multiply by the number of complete cycles
    complete_cycle_sum = m * (m - 1) / 2 * re
    
    # Sum of the remainder cycle (0 to c) is (c+1)*c/2
    remainder_cycle_sum = (c + 1) * c / 2
    
    # Return the total sum
    return complete_cycle_sum + remainder_cycle_sum

