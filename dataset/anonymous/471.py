def solution(a, b):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        sqrtn = int(n**0.5) + 1
        for i in range(5, sqrtn, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def end_one(n):
        while n > 6:
            n = sum(int(x) * int(x) for x in str(n))
            if n == 1:
                return True
        return False

    return sum(1 for n in range(a, b) if is_prime(n) and end_one(n))

