def find_largest_prime_factor_and_divisor(n: float) -> list:
    # Initialize variables
    bpf, bd = 0, 1
    frac = []
    
    # Check if n has a decimal part
    if n % 1 != 0:
        return "The number has a decimal part. No Results"
    else:
        # Convert n to an absolute integer
        n = abs(int(n))
        n_copy = n
  
    # Find prime factors
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            frac.append(i)
        else:
            i += 1
    if n > 1:
        frac.append(n)

    # Determine the largest prime factor and divisor
    bpf = max(frac)
    bd = n_copy / frac[0]
            
    # Return results based on conditions
    if bpf == 0 or bd == 1:
        return []
    else:
        return [bpf, bd]

