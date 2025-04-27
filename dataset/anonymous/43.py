def solution(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    solution(5, 2, 7) ➞ True
    
    solution(3, 2, 2) ➞ False

    solution(3, -2, 1) ➞ True
    
    solution(3.6, -2.2, 2) ➞ False
    '''

    if type(x) != int or type(y) != int or type(z) != int: return False
    return x == y + z or y == x + z or z == y + x

