def is_concatenated_sum_equal(n: int, r: int) -> bool:
    # Calculate the absolute value of n
    abs_n = abs(n)
    
    # Generate the concatenated sum
    concatenated_sum = sum(int(e * r) for e in str(abs_n))
    
    # Check if the concatenated sum equals the absolute value of n
    return abs_n == concatenated_sum

