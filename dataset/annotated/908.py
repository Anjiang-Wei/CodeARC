def match_brackets_positions(string: str) -> dict[int, int] | bool:
    brackets = {}
    open_brackets = []

    for i, c in enumerate(string):
        if c == '(':
            open_brackets.append(i)
        elif c == ')':
            if not open_brackets:
                return False
            brackets[open_brackets.pop()] = i

    # If there are unmatched open brackets, return False
    return False if open_brackets else brackets

