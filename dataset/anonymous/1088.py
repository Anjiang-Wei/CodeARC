def solution(n):
    import re
    # Use regex to find continuous parts of odd or even digits
    return [int(i) for i in re.findall(r"[2468]+|[13579]+", str(n))]

