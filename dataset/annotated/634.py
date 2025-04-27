def get_operator_classes(ari: bool = True, log: bool = True, cmp: bool = True) -> list:
    """Returns a list of operator class names based on selected categories."""
    
    ops = {
        "ari": ["Add", "Subtract", "Multiply", "Divide"],
        "log": ["And", "Or", "Not"],
        "cmp": ["Equal", "GreaterThan", "LessThan"],
    }
    
    res = []
    if ari:
        res.extend(ops["ari"])
    if log:
        res.extend(ops["log"])
    if cmp:
        res.extend(ops["cmp"])

    return res
