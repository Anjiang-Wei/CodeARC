def solution(sent, limit=1000):
    if not sent:
        return "No e-mails sent"
    elif sent >= limit:
        return "Daily limit is reached"
    return "{}%".format(int(sent * 100 / limit))

