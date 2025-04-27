def solution(full_text, search_text, allow_overlap=True):
    import re
    if not full_text or not search_text:
        return 0
    # Use a lookahead assertion for overlapping matches if allowed
    pattern = f'(?=({search_text}))' if allow_overlap else search_text
    matches = re.findall(pattern, full_text)
    return len(matches)

