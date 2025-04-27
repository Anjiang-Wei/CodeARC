def calculate_infection_percentage(s: str) -> float:
    lands = s.split('X')
    total = sum(map(len, lands))
    infected = sum(len(x) for x in lands if '1' in x)
    # Calculate the percentage of infected population
    return infected * 100 / (total or 1)

