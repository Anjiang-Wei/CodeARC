def solution(st):
    words = st.lower().split(' ')
    currentWord = None
    count = 0
    for i, word in enumerate(words):
        if i + 1 < len(words):
            if word == words[i + 1]:
                if word != currentWord:
                    currentWord = word
                    count += 1
            else:
                currentWord = None
    return count

