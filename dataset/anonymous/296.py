def solution(s):
    import re
    # Use regex to remove 'bug' not followed by 's'
    return re.sub(r'bug(?!s)', '', s)

