import cmath
from typing import Union

def calculate_phase_angle(a: Union[complex, float], b: Union[complex, float]) -> float:
    angle = cmath.phase(a + b)
    return angle

