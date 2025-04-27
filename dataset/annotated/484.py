def is_valid_datetime_format(date: str) -> bool:
    from re import match
    return bool(match(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', date))

