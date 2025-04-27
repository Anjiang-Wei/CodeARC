def are_elements_order_equivalent(a: list, b: list) -> bool:
    return [a.index(x) for x in a] == [b.index(y) for y in b]

