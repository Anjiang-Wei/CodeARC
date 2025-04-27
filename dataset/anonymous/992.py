def solution(m, n):
    def squared_cache(number, cache):
        if number not in cache:
            divisors = [x for x in range(1, number + 1) if number % x == 0]
            cache[number] = sum([x * x for x in divisors])
        return cache[number]

    cache = {}
    result = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number, cache)
        if (divisors_sum ** 0.5).is_integer():
            result.append([number, divisors_sum])

    return result

