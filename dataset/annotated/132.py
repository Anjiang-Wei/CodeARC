def join_tuple_elements_with_delimiter(test_tup: tuple) -> str:
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[: len(res) - len(delim)]
    return str(res)

