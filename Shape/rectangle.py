from .point import Point
from .line import Line
from .shape import Shape

# rectangle.py
class Rectangle(Shape):
    def __init__(self, init_type, *args):
        super().__init__(is_regular=False)
        if init_type not in [1, 2, 3]:
            raise ValueError("init_type debe ser 1, 2 o 3.")
        if init_type == 1:
            bottom_left, width, height = args
            self.width = width
            self.height = height
            self.center = Point(bottom_left.x + width/2, bottom_left.y + height/2)
        elif init_type == 2:
            center, width, height = args
            self.width = width
            self.height = height
            self.center = center
        elif init_type == 3:
            p1, p2 = args
            self.width = abs(p2.x - p1.x)
            self.height = abs(p2.y - p1.y)
            self.center = Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)
        self._build_shape()

    def _build_shape(self):
        left = self.center.x - self.width/2
        right = self.center.x + self.width/2
        bottom = self.center.y - self.height/2
        top = self.center.y + self.height/2
        bl = Point(left, bottom)
        br = Point(right, bottom)
        tr = Point(right, top)
        tl = Point(left, top)
        self.set_vertices([bl, br, tr, tl])
        e1 = Line(bl, br)
        e2 = Line(br, tr)
        e3 = Line(tr, tl)
        e4 = Line(tl, bl)
        self.set_edges([e1, e2, e3, e4])
        self.set_angles([90, 90, 90, 90])

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def inner_angles(self):
        return [90, 90, 90, 90]

    def contains_point(self, pt: Point):
        left = self.center.x - self.width/2
        right = self.center.x + self.width/2
        bottom = self.center.y - self.height/2
        top = self.center.y + self.height/2
        return left <= pt.x <= right and bottom <= pt.y <= top

    def intersects_line(self, p1: Point, p2: Point):
        # Para simplificar, verificamos si algún extremo de la línea está dentro del rectángulo
        if self.contains_point(p1) or self.contains_point(p2):
            return True
        return False
    