def solution(num):
    integer_part, fractional_part = str(num).split('.')

    # Process the integer part
    result = [str(int(digit) * (10 ** i)) for i, digit in enumerate(integer_part[::-1]) if digit != '0'][::-1]
    
    # Process the fractional part
    result += [f"{digit}/{10 ** (i + 1)}" for i, digit in enumerate(fractional_part) if digit != '0']

    # Join the results with ' + ' and return
    return ' + '.join(result)

