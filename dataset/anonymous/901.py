def solution(num):
    import re
    # Use regex to find odd numbers followed by odd numbers and insert a dash between them
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))

