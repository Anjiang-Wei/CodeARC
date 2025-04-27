def solution(digits):
    import re
    # Use regular expression to find all occurrences of English digits
    return ' '.join(re.findall('zero|one|two|three|four|five|six|seven|eight|nine', digits))

