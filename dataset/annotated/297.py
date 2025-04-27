def convert_fraction_to_mixed_number(fraction: str) -> str:
    n, d = [int(i) for i in fraction.split('/')]
    # Calculate the whole number part and the remainder
    whole_number = n // d
    remainder = n % d
    # Return the mixed number as a string
    return '{} {}/{}'.format(whole_number, remainder, d)

