def compare_real_numbers(a: int | float | str, b: int | float | str) -> int | float | str | None:
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_real_numbers(1, 2.5) ➞ 2.5
    compare_real_numbers(1, "2,3") ➞ "2,3"
    compare_real_numbers("5,1", "6") ➞ "6"
    compare_real_numbers("1", 1) ➞ None
    """

    num_a = float(str(a).replace(",", "."))
    num_b = float(str(b).replace(",", "."))
    if num_a == num_b:
        return None
    return a if num_a > num_b else b

