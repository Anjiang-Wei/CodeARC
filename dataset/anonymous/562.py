def solution(string, step):
    i = (step % len(string)) if string else 0
    return f"{string[-i:]}{string[:-i]}"
