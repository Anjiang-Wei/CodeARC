def compare_tuples_elementwise_is_greater(test_tup1: tuple, test_tup2: tuple) -> bool:
    return all(x > y for x, y in zip(test_tup1, test_tup2))

