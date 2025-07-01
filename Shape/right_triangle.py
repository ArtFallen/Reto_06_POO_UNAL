from .triangle import Triangle
from .point import Point

# right_triangle.py
class RightTriangle(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        angles_rounded = [round(angle, 5) for angle in self.angles]
        # Al menos un ángulo de 90 grados indica triángulo rectángulo
        self.is_regular = any(abs(angle - 90) < 1e-3 for angle in angles_rounded)
