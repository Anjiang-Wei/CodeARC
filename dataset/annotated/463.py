def random_case_string(s: str) -> str:
    import random
    return "".join([random.choice([c.lower(), c.upper()]) for c in s])

