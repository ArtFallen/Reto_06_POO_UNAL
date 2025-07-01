import math

# point.py
# Esta clase representa un punto en un plano cartesiano
class Point:
    def __init__(self, x_pos, y_pos):
        if not isinstance(x_pos, (int, float)) or not isinstance(y_pos, (int, float)):
            raise TypeError("Las coordenadas deben ser números (int o float).")
        self.x = x_pos
        self.y = y_pos

    def distance_to(self, other):
        # Calcula la distancia euclidiana entre dos puntos
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
