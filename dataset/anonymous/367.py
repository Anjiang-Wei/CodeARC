def solution(string_):
    def parse_character(char):
        # Check if character is uppercase
        if 65 <= ord(char) <= 90:
            return chr(155 - ord(char))
        # Check if character is lowercase
        elif 97 <= ord(char) <= 122:
            return chr(219 - ord(char))
        # Return character as is if not a letter
        else:
            return char

    # Check if input is a string
    if not isinstance(string_, str):
        return "Input is not a string"
    
    # Decode the string using the parse_character function
    return "".join(map(parse_character, string_))

