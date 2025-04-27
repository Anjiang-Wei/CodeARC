def calculate_typing_distance(words: str) -> int:
    H, W = 6, 8
    KEYBOARD = [
        "abcde123fghij456klmno789pqrst.@0uvwxyz_/\u000e ",
        "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/\u000e ",
        "^~?!'\"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡\u000e\u000e\u000e_/\u000e "
    ]
    MAP = [{c: (i // W, i % W) for i, c in enumerate(KEYBOARD[x])} for x in range(len(KEYBOARD))]

    def manhattan(*pts):
        dxy = [abs(z2 - z1) for z1, z2 in zip(*pts)]
        return 1 + sum(min(dz, Z - dz) for dz, Z in zip(dxy, (H, W)))

    cnt, mod, was = 0, 0, 'a'
    for c in words:
        while c not in KEYBOARD[mod]:
            cnt += manhattan(MAP[mod][was], MAP[mod]['\u000e'])
            was = '\u000e'
            mod = (mod + 1) % 3
        cnt += manhattan(MAP[mod][was], MAP[mod][c])
        was = c
    return cnt

