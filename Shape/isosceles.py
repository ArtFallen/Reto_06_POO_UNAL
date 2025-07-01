from .triangle import Triangle
from .point import Point

# isosceles.py
class Isosceles(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        lengths = [edge.length for edge in self.edges]
        # Dos lados iguales indica isósceles
        self.is_regular = lengths.count(lengths[0]) == 2 or lengths.count(lengths[1]) == 2
