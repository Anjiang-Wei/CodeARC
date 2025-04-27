def add_vectors(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
            
        def add(self, vector: 'Vector') -> 'Vector':
            return Vector(self.x + vector.x, self.y + vector.y)
    
    vector1 = Vector(x1, y1)
    vector2 = Vector(x2, y2)
    result_vector = vector1.add(vector2)
    
    return result_vector.x, result_vector.y

