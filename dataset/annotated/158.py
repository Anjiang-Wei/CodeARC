import cmath
from typing import Tuple

def convert_to_polar_and_rectangular(x: float, y: float) -> Tuple[Tuple[float, float], complex]:
    cn = cmath.polar(complex(x, y))
    cn1 = cmath.rect(2, cmath.pi)
    return (cn, cn1)

