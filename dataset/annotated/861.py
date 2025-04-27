def product_of_n_largest_elements(lst: list[int], n_largest_elements: int) -> int:
    from functools import reduce
    from operator import mul
    
    # Sort the list and take the n largest elements
    lst_largest = sorted(lst)[-n_largest_elements:]
    
    # Calculate the product of the n largest elements
    prod = reduce(mul, lst_largest, 1)
    
    return prod

