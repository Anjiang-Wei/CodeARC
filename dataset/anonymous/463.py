def solution(x):
    import random
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])

