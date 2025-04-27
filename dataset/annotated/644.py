def calculate_folds_to_reach_distance(distance: float) -> int:
    def fold_to(distance: float, thickness: float = 0.0001, folds: int = 0) -> int:
        if distance < 0:
            return None
        
        while thickness < distance:
            thickness *= 2
            folds += 1
        
        return folds
    
    return fold_to(distance)

