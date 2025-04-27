def check_alphabet_presence(st: str) -> str:
    # Convert input string to lowercase
    st = st.lower()
    # Initialize result string
    result = ""
    # Check presence of each letter in the alphabet
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter in st:
            result += "1"
        else:
            result += "0"
    return result

