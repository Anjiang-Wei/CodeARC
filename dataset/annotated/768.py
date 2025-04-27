def extract_unique_digits(s: str) -> str:
    from collections import OrderedDict

    # Filter digits and maintain order of first appearance
    digits = filter(str.isdigit, s)

    # Use OrderedDict to remove duplicates while preserving order
    unique_digits = "".join(OrderedDict.fromkeys(digits))

    # Return result or "One more run!" if no digits found
    return unique_digits or "One more run!"

