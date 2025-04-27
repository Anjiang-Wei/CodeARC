def solution(amount):
    import re
    m = re.match(r'\$(\d+)\.(\d\d)\Z', amount)
    return int(m.expand(r'\1\2')) if m else None

