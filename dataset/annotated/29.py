def count_vowels_in_word(s: str) -> int:
    """Write a function count_vowels_in_word which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> count_vowels_in_word("abcde")
    2
    >>> count_vowels_in_word("ACEDY")
    3
    """

    if s == "": return 0
    cnt = len(list(filter(lambda ch: ch in "aeiouAEIOU", s)))
    if s[-1] in "yY": cnt += 1
    return cnt

