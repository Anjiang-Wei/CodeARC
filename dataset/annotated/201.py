def remove_nested_tuples(test_tup: tuple) -> tuple:
    return tuple(e for e in test_tup if not isinstance(e, tuple))

