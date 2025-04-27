def solution(number, base):
    try:
        if base == 'hex':
            return hex(number)  # Convert to hexadecimal
        if base == 'bin':
            return bin(number)  # Convert to binary
    except:
        return 'Invalid number input'  # Handle invalid number input
    return 'Invalid base input'  # Handle invalid base input

