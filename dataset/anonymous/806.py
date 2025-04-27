def solution(x):
    return ''.join(filter(str.isdigit, x)) if isinstance(x, str) else 'Invalid input !'

