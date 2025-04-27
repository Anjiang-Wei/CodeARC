def solution(a, b):
    def factorize_add(num):
        if num < 4:
            return num
        d = 2
        p = 0
        while d <= num**0.5 + 1:
            while num % d == 0:
                p += d
                num /= d
            d += 1 if d == 2 else 2
        return p if num == 1 else p + num

    result = []
    for i in range(a, b + 1):
        r = factorize_add(i)
        if r != i and i % r == 0:
            result.append(i)
    return result

