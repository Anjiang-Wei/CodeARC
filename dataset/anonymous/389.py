def solution(s):
    # Separate vowels and non-vowels, then concatenate them
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))

