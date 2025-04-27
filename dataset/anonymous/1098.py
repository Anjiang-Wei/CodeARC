def solution(words):
    import re

    KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/* "
    MAP = {c: (i // 8, i % 8) for i, c in enumerate(KEYBOARD)}

    def manhattan(*pts):
        # Calculate the Manhattan distance between two points
        return 1 + sum(abs(z2 - z1) for z1, z2 in zip(*pts))

    def toggle(m):
        # Toggle Shift ON if uppercase presents, and then OFF if lowercase after
        ups, end = m.group(1), m.group(2)
        off = '*' * bool(end)
        return f'*{ups.lower()}{off}{end}'

    reWords = re.sub(r'([A-Z][^a-z]*)([a-z]?)', toggle, words)
    # Calculate total button presses required
    return sum(manhattan(MAP[was], MAP[curr]) for was, curr in zip('a' + reWords, reWords))

