def solution(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        solution(-12) ==> (1, 1)
        solution(123) ==> (1, 2)
    """

    even, odd = 0, 0
    for ch in str(abs(num)):
        if ch in "02468": even += 1
        if ch in "13579": odd += 1
    return even, odd

