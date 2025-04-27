def solution(text):
    text = text.strip()
    if len(text) < 1:
        return None
    else:
        if text[0] in '+-':
            text = text[1:]
        return text.isdigit()

