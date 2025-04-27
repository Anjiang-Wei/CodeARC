def calculate_total_pay(arr: list[int]) -> str:
    from math import ceil
    # Calculate total hours worked by summing cheese wheels and dividing by 100
    # Multiply by 35 to get total pay in pounds
    total_pay = ceil(sum(arr) / 100) * 35
    return f'£{total_pay}'

