from typing import List

def sort_string_by_custom_order(string: str, array: List[int]) -> str:
    # Sort the characters of the string based on the order specified by the array
    return "".join(v for _, v in sorted(zip(array, string)))

