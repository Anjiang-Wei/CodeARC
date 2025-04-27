def solution(string):
    def decipher_word(word):
        # Count the number of digits at the start of the word
        i = sum(map(str.isdigit, word))
        # Convert the digits to a character
        decoded = chr(int(word[:i]))
        # If the word has more than one character after the digits, swap the second and last characters
        if len(word) > i + 1:
            decoded += word[-1]
        # Add the middle part of the word and the second character
        if len(word) > i:
            decoded += word[i+1:-1] + word[i:i+1]
        return decoded

    # Split the string into words, decipher each word, and join them back into a string
    return ' '.join(map(decipher_word, string.split()))

