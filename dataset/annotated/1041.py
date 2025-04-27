def highlight_code_segments(code: str) -> str:
    import re
    # Highlight 'F' with pink
    code = re.sub(r"(F+)", '<span style="color: pink">\\g<1></span>', code)
    # Highlight 'L' with red
    code = re.sub(r"(L+)", '<span style="color: red">\\g<1></span>', code)
    # Highlight 'R' with green
    code = re.sub(r"(R+)", '<span style="color: green">\\g<1></span>', code)
    # Highlight digits with orange
    code = re.sub(r"(\d+)", '<span style="color: orange">\\g<1></span>', code)
    return code

