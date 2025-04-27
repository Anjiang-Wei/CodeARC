def calculate_missions_to_target(starting_number: float, reach: float, target: float) -> int:
    def recursive_missions(start: float, reach: float, target: float, missions: int = 0) -> int:
        if start >= target:
            return missions
        return recursive_missions(start + (start * reach), reach, target, missions + 1)
    
    return recursive_missions(starting_number, reach, target)

