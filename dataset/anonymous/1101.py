def solution(number):
    parts = str(number).split('98')

    return ', '.join(
        str(int(w, 2)) if i % 2 == 0 and all(c in '01' for c in w) else 
        ''.join(chr(65 + (int(w[x:x+3]) % 26)) for x in range(0, len(w), 3) if len(w[x:x+3]) == 3)
        for i, w in enumerate(parts) if w
    )

