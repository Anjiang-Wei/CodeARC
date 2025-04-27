def solution(x1, y1, x2, y2):
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def add(self, vector):
            return Vector(self.x + vector.x, self.y + vector.y)
    
    vector1 = Vector(x1, y1)
    vector2 = Vector(x2, y2)
    result_vector = vector1.add(vector2)
    
    return result_vector.x, result_vector.y

