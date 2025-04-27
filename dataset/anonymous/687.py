def solution(s):
    """
    :type s: str
    :rtype: bool
    """
    # Convert to lowercase and filter out non-alphanumeric characters
    cleanlist = [c for c in s.lower() if c.isalnum()]
    # Check if the cleaned list is equal to its reverse
    return cleanlist == cleanlist[::-1]

