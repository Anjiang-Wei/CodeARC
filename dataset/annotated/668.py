def email_status(sent: int, limit: int = 1000) -> str:
    if not sent:
        return "No e-mails sent"
    elif sent >= limit:
        return "Daily limit is reached"
    return "{}%".format(int(sent * 100 / limit))

