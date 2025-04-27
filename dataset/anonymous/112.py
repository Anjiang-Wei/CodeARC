def solution(list1, element):
    list1 = [v for elt in list1 for v in (element, elt)]
    return list1

