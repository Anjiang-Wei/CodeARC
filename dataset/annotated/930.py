def compute_operation(v: dict) -> float:
    return {
        "+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a'] ** v['b'],
    }.get(v['operation'])

