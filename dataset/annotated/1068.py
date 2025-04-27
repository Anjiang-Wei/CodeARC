def translate_using_keyword(s: str, keyword: str) -> str:
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for c in keyword + abc:
        if c not in key:
            key += c
    # Translate the string using the created key
    return s.lower().translate(str.maketrans(abc, key))

