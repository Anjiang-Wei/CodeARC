def find_substring_index(haystack: str, needle: str) -> int:
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # Handle the case where both haystack and needle are empty
    if haystack == "" and needle == "":
        return 0
    # Handle the case where needle is empty
    if needle == "":
        return 0
    # Handle cases where haystack is empty or needle is not found in haystack
    if haystack == "" or len(haystack.split(needle)) == 1:
        return -1
    # Return the index of the first occurrence of needle in haystack
    return len(haystack.split(needle)[0])

