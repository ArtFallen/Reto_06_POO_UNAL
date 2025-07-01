from .point import Point
from .line import Line

# shape.py
class Shape:
    def __init__(self, is_regular=False):
        self.is_regular = is_regular
        self.vertices = []
        self.edges = []
        self.angles = []

    def set_vertices(self, points_list):
        if not points_list or not all(isinstance(p, Point) for p in points_list):
            raise ValueError("Debe proporcionar una lista válida de objetos Point.")
        self.vertices = points_list

    def set_edges(self, lines_list):
        if not lines_list or not all(isinstance(l, Line) for l in lines_list):
            raise ValueError("Debe proporcionar una lista válida de objetos Line.")
        self.edges = lines_list


    def set_angles(self, angles_list):
        self.angles = angles_list

    def area(self):
        # Método base, se sobrescribe en clases hijas
        return None

    def perimeter(self):
        total = 0
        for edge in self.edges:
            total += edge.length
        return total

    def inner_angles(self):
        # Método base, se sobrescribe en clases hijas
        return None
    