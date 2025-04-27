def solution(s=''):
    # Check if the input is a string
    if isinstance(s, str):
        # Count vowels by checking each character
        return sum(x.lower() in 'aeoui' for x in s)
    else:
        # Return None for non-string inputs
        return None

