def roll_dice(desc: str, verbose: bool = False) -> bool or dict or int:
    import re, random
    
    if not isinstance(desc, str):
        return False
    
    # Remove whitespace and match the pattern
    ans = re.findall(r'^(\d*)d(\d+)(([+\-]\d+)*)$', desc.replace(' ', ''))
    
    if len(ans) == 0:
        return False
    
    # Parse the matched groups into a dictionary
    dct = {i: eval(v) for i, v in enumerate(ans[0]) if v}
    
    # Roll the dice and calculate the modifier
    dices = {
        'dice': [1 + random.randrange(dct[1]) for _ in range(dct.get(0, 1))],
        'modifier': dct.get(2, 0)
    }
    
    # Return verbose or summed result
    return dices if verbose else sum(dices['dice']) + dices['modifier']

