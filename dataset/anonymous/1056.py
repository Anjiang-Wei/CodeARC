def solution(roots):
    import re

    def deploy(roots):
        r = -roots[0]
        if len(roots) == 1:
            return [r, 1]
        
        sub = deploy(roots[1:]) + [0]
        return [c * r + sub[i - 1] for i, c in enumerate(sub)]
    
    coefs = deploy(roots)
    poly = ' + '.join(["{}x^{}".format(c, i) for i, c in enumerate(coefs) if c][::-1])
    # Remove unnecessary parts of the polynomial string
    poly = re.sub(r'x\^0|\^1\b|\b1(?=x)(?!x\^0)', '', poly).replace("+ -", "- ") + ' = 0'
    return poly

