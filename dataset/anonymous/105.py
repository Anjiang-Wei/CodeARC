def solution(test_tuple):
    return all(isinstance(item, type(test_tuple[0])) for item in test_tuple)

