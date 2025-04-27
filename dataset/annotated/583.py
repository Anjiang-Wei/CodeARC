def find_unique_date(a: int, b: int, c: int) -> str:
    from datetime import datetime
    from itertools import permutations

    dates = set()
    for p in permutations((a, b, c)):
        try:
            date = '{:02}/{:02}/{:02}'.format(*p)
            datetime.strptime(date, '%y/%m/%d')
            dates.add(date)
        except ValueError:
            pass

    if len(dates) == 1:
        return dates.pop()
    elif dates:
        return "ambiguous"
    else:
        return "invalid"

