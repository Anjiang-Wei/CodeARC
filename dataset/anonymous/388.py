def solution(words):
    import re

    H, W = 6, 8
    KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/* "
    MAP = {c: (i // W, i % W) for i, c in enumerate(KEYBOARD)}

    def manhattan(*pts):
        dxy = [abs(z2 - z1) for z1, z2 in zip(*pts)]
        return 1 + sum(min(dz, Z - dz) for dz, Z in zip(dxy, (H, W)))

    def toggle(m):
        ups, end = m.groups()
        return f'*{ups.lower()}*{end}'

    reWords = re.sub(r'([A-Z][^a-z]*)([a-z]?)', toggle, words).rstrip('*')
    return sum(manhattan(MAP[was], MAP[curr]) for was, curr in zip('a' + reWords, reWords))

