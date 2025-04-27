def solution(fen_string):
    from pprint import pprint

    uni = {
        'q': '\u2655', 'B': '\u265D', 'p': '\u2659', 'K': '\u265A',
        'N': '\u265E', 'Q': '\u265B', 'P': '\u265F', 'R': '\u265C',
        'n': '\u2658', 'r': '\u2656', 'b': '\u2657', 'k': '\u2654',
        1: "\u2587", 0: "\uFF3F"
    }

    def parse_fen(string):
        board = [[1, 0, 1, 0, 1, 0, 1, 0] if not i % 2 else [0, 1, 0, 1, 0, 1, 0, 1] for i in range(8)]

        col, row = 0, 0
        pos = 0
        placement, turn = string.split(" ")[:2]

        while pos < len(placement):
            if placement[pos] == "/":
                row += 1
                col = 0
            elif placement[pos].isdigit():
                col += int(placement[pos])
            else:
                board[row][col] = uni[placement[pos]]
                col += 1
            pos += 1

        board = [[uni[i] if type(i) is int else i for i in x] for x in board]

        if turn == "b":
            board = [list(v)[::-1] for v in zip(*[i[::-1] for i in zip(*board)])]

        return "\n".join(["".join(i) for i in board]) + "\n"

    return parse_fen(fen_string)

