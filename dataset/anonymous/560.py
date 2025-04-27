def solution(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

