def solution(starting_number, reach, target):
    def recursive_missions(start, reach, target, missions=0):
        if start >= target:
            return missions
        return recursive_missions(start + (start * reach), reach, target, missions + 1)
    
    return recursive_missions(starting_number, reach, target)

