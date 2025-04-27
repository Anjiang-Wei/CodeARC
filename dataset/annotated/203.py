def calculate_sum_of_odds_in_range(l: int, r: int) -> int:
    def sum_odd(n: int) -> int:
        terms = (n + 1) // 2
        sum1 = terms * terms
        return sum1

    return sum_odd(r) - sum_odd(l - 1)

