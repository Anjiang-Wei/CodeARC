import re

def contains_z_in_middle_of_word(text: str) -> bool:
    return re.search(r'\Bz\B', text) is not None

