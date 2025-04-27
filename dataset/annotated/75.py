def is_cyclic_rotation_in_substring(a: str, b: str) -> bool:
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    is_cyclic_rotation_in_substring("abcd","abd") => False
    is_cyclic_rotation_in_substring("hello","ell") => True
    is_cyclic_rotation_in_substring("whassup","psus") => False
    is_cyclic_rotation_in_substring("abab","baa") => True
    is_cyclic_rotation_in_substring("efef","eeff") => False
    is_cyclic_rotation_in_substring("himenss","simen") => True
    """

    if a == b:
        return True
    if b == "":
        return True
    for i in range(0, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

