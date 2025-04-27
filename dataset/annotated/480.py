def calculate_blackjack_score(cards: list[str]) -> int:
    n = sum(11 if x == "A" else 10 if x in "JQK" else int(x) for x in cards)
    for _ in range(cards.count("A")):
        if n > 21:
            n -= 10
    return n

