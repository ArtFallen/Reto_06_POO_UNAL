from .triangle import Triangle
from .point import Point

# scalene.py
class Scalene(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        lengths = [edge.length for edge in self.edges]
        # Todos los lados diferentes indica escaleno
        self.is_regular = len(set(lengths)) == 3
        