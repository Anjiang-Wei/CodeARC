def find_matching_multiplier(k1: int) -> int:
    k2, n = k1 + 1, 1

    def digits(n: int) -> list:
        # Returns the sorted list of digits of the number n
        return sorted(str(n))
    
    # Increment n until the digits of n*k1 and n*k2 match
    while digits(n * k1) != digits(n * k2):
        n += 1
    
    return n

