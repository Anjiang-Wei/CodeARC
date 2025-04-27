def count_matching_char_positions(input_string: str) -> int:
    return sum(ord(ch.lower()) - ord('a') == i for i, ch in enumerate(input_string))

