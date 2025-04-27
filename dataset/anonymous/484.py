def solution(date):
    from re import match
    return bool(match(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', date))

