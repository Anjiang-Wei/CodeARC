def solution(word):
    def char_concat(word, index=1):
        if len(word) < 2:
            return ''
        # Concatenate first and last character with the index
        return word[0] + word[-1] + str(index) + char_concat(word[1:-1], index + 1)
    
    return char_concat(word)

