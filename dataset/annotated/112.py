def interleave_elements_with_value(list1: list, element) -> list:
    list1 = [v for elt in list1 for v in (element, elt)]
    return list1

