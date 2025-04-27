def solution(v):
    return {
        "+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a'] ** v['b'],
    }.get(v['operation'])

