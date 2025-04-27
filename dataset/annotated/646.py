def convert_to_upper_vowels(st: str) -> str:
    tr = str.maketrans('aeiou', 'AEIOU')
    return st.translate(tr)

