from .shape import Shape
from .line import Line
from .point import Point
import math

# triangle.py
class Triangle(Shape):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(is_regular=False)
        self.set_vertices([point1, point2, point3])
        l1 = Line(point1, point2)
        l2 = Line(point2, point3)
        l3 = Line(point3, point1)
        self.set_edges([l1, l2, l3])
        self.angles = self.inner_angles()

    def inner_angles(self):
        a, b, c = [edge.length for edge in self.edges]
        try:
            angle1 = math.degrees(math.acos((b*b + c*c - a*a) / (2 * b * c)))
            angle2 = math.degrees(math.acos((a*a + c*c - b*b) / (2 * a * c)))
        except ValueError:
            raise ValueError("Los puntos del triángulo no forman un triángulo válido (¿colineales?).")
        angle3 = 180 - angle1 - angle2
        return [angle1, angle2, angle3]

    def area(self):
        a, b, c = [edge.length for edge in self.edges]
        s = (a + b + c) / 2
        area_val = s * (s - a) * (s - b) * (s - c)
        if area_val > 0:
            return math.sqrt(area_val)
        else:
            return 0
