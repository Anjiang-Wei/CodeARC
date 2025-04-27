def is_whole_number_multiplication(x: str, n: str) -> bool:
    """Your task is to implement a function to determine if the multiplication
    of two fractions evaluates to a whole number. The function returns True 
    if x * n evaluates to a whole number and False otherwise. Both x and n are
    string representations of a fraction in the format <numerator>/<denominator> 
    where both numerator and denominator are positive whole numbers.

    You can assume that x and n are valid fractions, and do not have zero as a denominator.

    Examples:
    is_whole_number_multiplication("1/5", "5/1") = True
    is_whole_number_multiplication("1/6", "2/1") = False
    is_whole_number_multiplication("7/10", "10/2") = False
    """

    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    return (x1 * n1) % (x2 * n2) == 0

