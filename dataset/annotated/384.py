def count_occurrences(full_text: str, search_text: str, allow_overlap: bool = True) -> int:
    import re
    if not full_text or not search_text:
        return 0
    # Use a lookahead assertion for overlapping matches if allowed
    pattern = f'(?=({search_text}))' if allow_overlap else search_text
    matches = re.findall(pattern, full_text)
    return len(matches)

