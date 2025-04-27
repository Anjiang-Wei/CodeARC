def solution(numbers):
    from functools import reduce
    from operator import mul
    return reduce(mul, numbers) if numbers else None

