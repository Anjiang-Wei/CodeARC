def rearrange_string_after_iterations(s: str, n: int) -> str:
    iterations = [s]
    
    while True:
        # Concatenate even-indexed chars to the front, odd-indexed chars to the back
        s = s[::2] + s[1::2]
        # Check if the string has returned to its original form
        if s == iterations[0]: 
            break
        iterations.append(s)
    
    # Return the result after n iterations, using modulo to handle large n
    return iterations[n % len(iterations)]

