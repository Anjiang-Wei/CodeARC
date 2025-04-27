def solution(shoal):
    eaten, size, target = 0, 1, 4
    for f in sorted(map(int, shoal)):
        if f > size:
            break
        eaten += f
        if eaten >= target:
            size += 1
            target += 4 * size
    return size

