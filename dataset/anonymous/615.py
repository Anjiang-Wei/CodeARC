def solution(s):
    """
    :type s: str
    :rtype: str
    """
    # Filter out non-alphabetic characters and sort the remaining characters
    # in a case-insensitive manner, then join them into a single string.
    return "".join(sorted(filter(str.isalpha, s), key=str.lower))

