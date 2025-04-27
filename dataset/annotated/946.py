def swap_case_based_on_binary(s: str, n: int) -> str:
    from itertools import cycle
    
    # Create a cycle of the binary representation of n, skipping the '0b' prefix
    b = cycle(bin(n)[2:])
    
    # Swap case for alphabetic characters based on the current bit, otherwise keep the character as is
    return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)

