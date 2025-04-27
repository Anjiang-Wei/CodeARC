def has_repeating_subpattern(string: str) -> bool:
    from collections import Counter
    from functools import reduce
    from math import gcd

    # Calculate the greatest common divisor of the counts of each character
    # If the GCD is greater than 1, a subpattern exists
    return reduce(gcd, Counter(string).values()) != 1

