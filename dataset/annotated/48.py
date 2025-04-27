def split_into_words(s: str) -> list[str]:
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    split_into_words("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    split_into_words("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    words = (s.replace(",", " ")).split()
    return [word for word in words if word != ""]

