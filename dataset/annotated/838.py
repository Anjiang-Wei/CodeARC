from typing import List

def determine_tictactoe_winner(moves: List[List[int]]) -> str:
    # player one and two moves
    player_a, player_b = moves[0::2], moves[1::2]

    # possible wins
    possible_wins = {
        0: [[0, 0], [1, 1], [2, 2]],
        1: [[0, 0], [1, 0], [2, 0]],
        2: [[0, 1], [1, 1], [2, 1]],
        3: [[0, 2], [1, 2], [2, 2]],
        4: [[0, 0], [0, 1], [0, 2]],
        5: [[1, 0], [1, 1], [1, 2]],
        6: [[2, 0], [2, 1], [2, 2]],
        7: [[0, 2], [1, 1], [2, 0]]
    }

    # count player one and two correct moves
    for possible_win in possible_wins.values():
        count_a = 0
        for move in player_a:
            if move in possible_win:
                count_a += 1
            if count_a == 3:
                return 'A'

        count_b = 0
        for move in player_b:
            if move in possible_win:
                count_b += 1
            if count_b == 3:
                return 'B'

    return 'Draw' if len(player_a) + len(player_b) == 9 else 'Pending'

