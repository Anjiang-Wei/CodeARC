def is_happy_string(s: str) -> bool:
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy_string(a) => False
    is_happy_string(aa) => False
    is_happy_string(abcd) => True
    is_happy_string(aabb) => False
    is_happy_string(adb) => True
    is_happy_string(xyy) => False
    """
    
    if len(s) < 3: return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True

