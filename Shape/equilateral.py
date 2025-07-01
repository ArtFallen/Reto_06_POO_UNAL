from .point import Point
from .triangle import Triangle

# equilateral.py
class Equilateral(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        lengths = [round(edge.length, 5) for edge in self.edges]
        # Todos los lados iguales indica equilátero
        self.is_regular = all(l == lengths[0] for l in lengths)
        