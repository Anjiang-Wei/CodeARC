def are_anagrams(test: str, original: str) -> bool:
    return sorted(original.lower()) == sorted(test.lower())

