def calculate_years_to_reach_population(
    p0: int, percent: float, aug: int, p: int
) -> int:
    year = 0
    while p0 < p:
        p0 += p0 * percent / 100.0 + aug
        year += 1
    return year

