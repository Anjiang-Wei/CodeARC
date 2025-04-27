def is_robot_back_to_origin(moves: str) -> bool:
    """
    :type moves: str
    :rtype: bool
    """
    # Check if the number of 'U' moves equals 'D' moves and 'L' moves equals 'R' moves
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

