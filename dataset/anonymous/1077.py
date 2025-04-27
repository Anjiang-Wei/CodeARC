def solution(text):
    CONSONANTS = set('bcdfghjklmnpqrstvwxyz')
    # Convert text to lowercase and find intersection with consonants
    return len(CONSONANTS.intersection(text.lower()))

