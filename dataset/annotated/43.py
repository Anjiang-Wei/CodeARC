def is_sum_of_others(x: int, y: int, z: int) -> bool:
    '''
    Create a function that takes 3 integers.
    Returns true if one of the integers is equal to the sum of the other two.
    Returns false in any other cases.
    
    Examples
    is_sum_of_others(5, 2, 7) ➞ True
    
    is_sum_of_others(3, 2, 2) ➞ False

    is_sum_of_others(3, -2, 1) ➞ True

    is_sum_of_others(3.6, -2.2, 2) ➞ False (invalid input, function expects integers only)
    '''

    if type(x) != int or type(y) != int or type(z) != int: return False
    return x == y + z or y == x + z or z == y + x

