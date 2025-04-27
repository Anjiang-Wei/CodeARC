import math
from typing import Union

def calculate_hypotenuse(w: Union[int, float], h: Union[int, float]) -> float:
    return math.sqrt(w * w + h * h)

