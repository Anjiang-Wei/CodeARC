def describe_number(x: int) -> str:
    result = "{0} is more than zero." if x > 0 else "{0} is equal to or less than zero."
    return result.format(x)

