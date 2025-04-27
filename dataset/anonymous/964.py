def solution(lower_limit, upper_limit):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        return all(n % d for d in range(3, int(n ** 0.5) + 1, 2))

    a_p = []
    for n in range(lower_limit | 1, upper_limit, 2):
        for gap in range(30, (upper_limit - n) // 5 + 1, 30):
            sequence = [n + i * gap for i in range(6)]
            if all(is_prime(num) for num in sequence):
                a_p.append(sequence)
    return a_p

