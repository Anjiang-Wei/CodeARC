def identify_case_type(c_str: str) -> str:
    import re

    # Define the regex patterns for each case type
    cases = [
        ('snake', re.compile(r'\A[a-z]+(_[a-z]+)+\Z')),
        ('kebab', re.compile(r'\A[a-z]+(-[a-z]+)+\Z')),
        ('camel', re.compile(r'\A[a-z]+([A-Z][a-z]*)+\Z')),
        ('none', re.compile(r'\A\Z')),
    ]

    # Check the input string against each pattern
    for case, pattern in cases:
        if pattern.match(c_str):
            return case

