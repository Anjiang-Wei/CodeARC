def determine_battle_outcome(fight: str) -> str:
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1,
         'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(d[c] for c in fight if c in d)
    
    # Determine the result based on the sum of powers
    return {
        r == 0: "Let's fight again!",
        r > 0: "Left side wins!",
        r < 0: "Right side wins!"
    }[True]

