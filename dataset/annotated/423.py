def max_product_of_five_consecutive_digits(n: str) -> int:
    from itertools import islice
    from functools import reduce

    numbers = [int(value) for value in n]
    result = [reduce(lambda x, y: x * y, islice(numbers, i, i + 5), 1) for i in range(len(numbers) - 4)]
    
    return max(result)

