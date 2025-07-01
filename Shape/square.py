from .point import Point
from .rectangle import Rectangle

# square.py
class Square(Rectangle):
    def __init__(self, center: Point, side_length: float):
        if side_length <= 0:
            raise ValueError("El lado del cuadrado debe ser un número positivo.")
        super().__init__(2, center, side_length, side_length)
        self.is_regular = True
