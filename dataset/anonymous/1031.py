def solution(s):
    TOME = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
        'k': 10, 'l': 20, 'm': 30, 'n': 40, 'o': 50, 'p': 60, 'q': 70, 'r': 80, 
        's': 90, 't': 100, 'u': 200, 'x': 300, 'y': 400, 'z': 500, 'j': 600, 
        'v': 700, 'w': 900
    }
    # Calculate the gematrian value by summing the values of each character
    return sum(TOME.get(c, 0) for c in s.lower())

