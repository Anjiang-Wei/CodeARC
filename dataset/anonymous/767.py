def solution(blocks):
    for _ in range(4):
        if 4 in blocks:
            blocks.remove(4)
        elif 3 in blocks and 1 in blocks:
            blocks.remove(3)
            blocks.remove(1)
        elif blocks.count(2) >= 2:
            blocks.remove(2)
            blocks.remove(2)
        elif 2 in blocks and blocks.count(1) >= 2:
            blocks.remove(2)
            blocks.remove(1)
            blocks.remove(1)
        elif blocks.count(1) >= 4:
            blocks.remove(1)
            blocks.remove(1)
            blocks.remove(1)
            blocks.remove(1)
        else:
            return False
    return True

