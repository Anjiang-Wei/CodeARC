from typing import List

def calculate_max_nesting_depth(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> calculate_max_nesting_depth('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    def count_depth(s: str) -> int:
        max_depth, cnt = 0, 0
        for ch in s:
            if ch == "(": cnt += 1
            if ch == ")": cnt -= 1
            max_depth = max(max_depth, cnt)
        return max_depth
    
    return [count_depth(s) for s in paren_string.split(" ") if s != ""]

