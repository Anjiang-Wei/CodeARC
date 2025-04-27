def find_common_substrings(arr: list[str]) -> str:
    import re

    # Find all common substrings between consecutive words
    common = re.findall(r'(.+) (?=\1)', ' '.join(arr))
    
    # Check if the number of common substrings is one less than the number of words
    return ''.join(common) if len(common) + 1 == len(arr) else 'failed to mesh'

