def calculate_grade(score1: float, score2: float, score3: float) -> str:
    m = (score1 + score2 + score3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return 'F'

