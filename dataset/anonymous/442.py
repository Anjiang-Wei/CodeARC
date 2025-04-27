def solution(text):
    # Find the position of the opening parenthesis and add 1 to get the start of the area code
    start = text.find("(") + 1
    # Find the position of the closing parenthesis to get the end of the area code
    end = text.find(")")
    # Return the substring that represents the area code
    return text[start:end]

