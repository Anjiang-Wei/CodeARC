def sort_anagram_words(s: str) -> str:
    words = [''.join(sorted(word)) for word in s.split()]
    words.sort(key=lambda word: (sum(map(ord, word)), len(word), word))
    return ' '.join(words)

