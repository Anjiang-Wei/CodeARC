def solution(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for solution(7, 34, 12) == 34
    for solution(15, 8, 5) == 5
    """

    def is_prime(a):
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))
    
    return x if is_prime(n) else y

