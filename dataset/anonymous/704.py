def solution(s):
    """
    :type s: str
    :rtype: int
    """
    # Convert the string to lowercase and use a set to find unique characters
    # Count how many of these characters appear more than once
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

