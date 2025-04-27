def solution(distance):
    def fold_to(distance, thickness=0.0001, folds=0):
        if distance < 0:
            return None
        
        while thickness < distance:
            thickness *= 2
            folds += 1
        
        return folds
    
    return fold_to(distance)

