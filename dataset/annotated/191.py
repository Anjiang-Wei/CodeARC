def symmetric_difference(list1: list, list2: list) -> list:
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))

