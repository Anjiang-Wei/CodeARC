def solution(arr: list) -> str:
    import re

    # Identify invalid entries
    invalid_entries = [e for e in arr if not re.match(r'(None)|([+-]?\d+)', str(e))]
    
    # Return message if there are invalid entries
    if len(invalid_entries) == 1:
        return f'There is 1 invalid entry: {invalid_entries[0]}'
    if len(invalid_entries) > 1:
        return f'There are {len(invalid_entries)} invalid entries: {invalid_entries}'

    # Custom implementation of gcd
    def custom_gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    # Custom implementation of lcm
    def lcm(a, b):
        a, b = abs(int(a or 1)), abs(int(b or 1))  # Convert None to 1, ensure non-negative
        return a * b // custom_gcd(a, b)

    # Compute LCM iteratively
    result = 1
    for num in arr:
        result = lcm(result, num)

    return str(result)

