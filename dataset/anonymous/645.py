def solution(a, b):
    # Check if both a and b are integers
    if isinstance(a, int) and isinstance(b, int):
        # Return the sum of a % b and b % a
        return a % b + b % a
    else:
        # Return False if either a or b is not an integer
        return False

