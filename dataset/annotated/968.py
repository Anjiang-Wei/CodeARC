def format_differences_from_first(arr: list[int]) -> list[str]:
    return ["{:+d}".format(i - arr[0]) for i in arr]

