from typing import List

def determine_grade(scores: List[float]) -> str:
    from bisect import bisect
    from statistics import mean
    
    # Calculate the mean score and determine the grade using bisect
    return 'FDCBA'[bisect([60, 70, 80, 90], mean(scores))]

