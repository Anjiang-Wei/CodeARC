def convert_string_to_word_list(string: str) -> list[str]:
    return string.split(" ")

def main():
    string = "Your input string here"
    result = convert_string_to_word_list(string)
    print(result)

if __name__ == "__main__":
    main()

