def solution(text):
    import re

    # Pattern to match syllables, considering silent 'e'
    pattern = re.compile(r'[aeyuio]+[^aeyuio ]*((?=e\b)e)?', flags=re.I)
    
    def check(s):
        return sum(1 for _ in pattern.finditer(s))

    # Split the text into lines and check syllable count
    return [5, 7, 5] == [check(s) for s in text.split("\n")]

