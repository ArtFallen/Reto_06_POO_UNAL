from .point import Point

# line.py
class Line:
    def __init__(self, start_point, end_point):
        if not all(isinstance(p, Point) for p in [start_point, end_point]):
            raise TypeError("start_point y end_point deben ser objetos Point.")
        self.start = start_point
        self.end = end_point
        self.length = self.start.distance_to(self.end)
