def arrange_to_form_largest_number(numbers: list[int]) -> int:
    from functools import cmp_to_key
    
    # Custom comparator to decide the order based on concatenated results
    cmp = lambda a, b: int(f'{b}{a}') - int(f'{a}{b}')
    
    # Sort numbers using the custom comparator and join them to form the largest number
    largest_arrangement = int(''.join(str(i) for i in sorted(numbers, key=cmp_to_key(cmp))))
    
    return largest_arrangement

