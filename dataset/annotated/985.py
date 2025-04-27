def product_except_self(numbers: list[int]) -> list[int]:
    from operator import mul
    from functools import reduce
    
    # Calculate the total product of all numbers
    tot = reduce(mul, numbers)
    
    # Return a new list where each element is the total product divided by the element at that index
    return [tot // n for n in numbers]

