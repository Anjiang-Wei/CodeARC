from typing import List, Tuple

def rectangles_overlap(rec1: List[int], rec2: List[int]) -> bool:
    return not (rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1])

