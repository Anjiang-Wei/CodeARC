def solution(room_length, room_width, roll_width, roll_cost):
    x, y = sorted((room_length, room_width))
    if y == 0 or x > roll_width:
        return "error"
    if y < roll_width:
        return round(x * roll_width * roll_cost, 2)
    return round(y * roll_width * roll_cost, 2)

