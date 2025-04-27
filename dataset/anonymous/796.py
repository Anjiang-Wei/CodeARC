def solution(lst):
    return ["empty", "singleton", "longer"][min(len(lst), 2)]

