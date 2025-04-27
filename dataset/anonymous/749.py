def solution(s):
    """
    :type s: str
    :rtype: str
    """
    # Remove spaces (ghosts) from the string
    # If there are no spaces, return the autograph message
    return s.replace(' ', '') if ' ' in s else "You just wanted my autograph didn't you?"

