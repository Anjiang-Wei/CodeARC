def is_cube(n: int) -> bool:
    '''
    Write a function that takes an integer n and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    is_cube(1) ==> True
    is_cube(2) ==> False
    is_cube(-1) ==> True
    is_cube(64) ==> True
    is_cube(0) ==> True
    is_cube(180) ==> False
    '''

    n = abs(n)
    return int(round(n ** (1. / 3))) ** 3 == n

