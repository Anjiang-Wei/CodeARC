def can_construct_ransom_note_from_magazine(ransomNote: str, magazine: str) -> bool:
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # Create a set of unique characters in the ransom note
    ransome = set(ransomNote)
    
    # Check if each character in the ransom note can be constructed from the magazine
    for i in ransome:
        if ransomNote.count(i) > magazine.count(i):
            return False
    
    return True

