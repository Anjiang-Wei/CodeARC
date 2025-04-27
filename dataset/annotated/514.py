def check_prime_digit_constraints(a: int, b: int) -> None:
    from math import sqrt

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for x in range(2, int(sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True

    def all_dig_prime(n: int) -> bool:
        for d in str(n):
            if d not in "2357":
                return False
        return True

    # Any additional code or logic related to the intended use of `is_prime` and `all_dig_prime`
    # should be included here if necessary

