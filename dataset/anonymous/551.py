def solution(string, prefix):
    """
    :type string: str
    :type prefix: str
    :rtype: int
    """
    # Check if the string starts with the prefix
    return 1 if string.startswith(prefix) else 0

