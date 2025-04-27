def count_unique_consonants(text: str) -> int:
    CONSONANTS = set('bcdfghjklmnpqrstvwxyz')
    # Convert text to lowercase and find intersection with consonants
    return len(CONSONANTS.intersection(text.lower()))

