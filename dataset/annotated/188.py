def is_valid_decimal_number(num: str) -> bool:
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    return dnumre.search(num) is not None

