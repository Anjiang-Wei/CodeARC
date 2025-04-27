def construct_indexed_pairs(word: str) -> str:
    def char_concat(word: str, index: int = 1) -> str:
        if len(word) < 2:
            return ''
        # Concatenate first and last character with the index
        return word[0] + word[-1] + str(index) + char_concat(word[1:-1], index + 1)
    
    return char_concat(word)

