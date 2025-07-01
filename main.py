from Shape import Point, Rectangle, Square, Triangle, Isosceles, Equilateral, Scalene, RightTriangle
import math

def main():
    try:
        # Punto de prueba
        p1 = Point(0, 0)
        p2 = Point(4, 0)
        p3 = Point(0, 3)

        # Triángulo
        tri = Triangle(p1, p2, p3)
        print("Área del triángulo:", tri.area())
        print("Ángulos del triángulo:", tri.inner_angles())

        # Rectángulo
        rect = Rectangle(3, p1, p2)  # init_type=3, con dos puntos
        print("Perímetro del rectángulo:", rect.perimeter())
        print("Área del rectángulo:", rect.area())

        # Cuadrado
        center = Point(5, 5)
        square = Square(center, 4)
        print("¿Contiene el punto (6,6)?", square.contains_point(Point(6, 6)))

        # Triángulos especiales
        iso = Isosceles(p1, p2, Point(2, 3))
        print("Isósceles regular:", iso.is_regular)

        eq = Equilateral(Point(0, 0), Point(1, math.sqrt(3)), Point(2, 0))
        print("Equilátero regular:", eq.is_regular)

        scal = Scalene(p1, Point(3, 2), Point(2, 5))
        print("Escaleno regular:", scal.is_regular)

        rt = RightTriangle(p1, p2, p3)
        print("Triángulo rectángulo:", rt.is_regular)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
