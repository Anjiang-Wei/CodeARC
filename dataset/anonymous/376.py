def solution(dice_set):
    import numpy as np

    def products(n, min_divisor, max_divisor):
        if n == 1:
            yield []
        for divisor in range(min_divisor, max_divisor + 1):
            if n % divisor == 0:
                for product in products(n // divisor, divisor, max_divisor):
                    yield product + [divisor]

    product = np.prod(dice_set)
    possible_sets = list(products(product, 3, min(product - 1, 20)))
    
    # Subtract 1 to exclude the original set itself if it has more than one die
    return len(possible_sets) - 1 if len(dice_set) > 1 else len(possible_sets)

