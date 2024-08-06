# TODO: Add code here
import matplotlib.pyplot as plt
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y



def __str__(self):
    return f"Point({self.x}, {self.y})"


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"

  class Point:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Point({self.x}, {self.y})"

    class Triangle:
        def __init__(self, point_1: Point, point_2: Point, point_3: Point):
            self.point_1 = point_1
            self.point_2 = point_2
            self.point_3 = point_3

        def area(self) -> float:
            # Usando la fórmula de área de un triángulo con coordenadas de vértices
            x1, y1 = self.point_1.x, self.point_1.y
            x2, y2 = self.point_2.x, self.point_2.y
            x3, y3 = self.point_3.x, self.point_3.y
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

        def draw(self):
            x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
            y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
            plt.fill(x, y, color='b', alpha=0.5)
            plt.plot(x, y, 'bo-')  # Añade los puntos y bordes
            plt.axis("scaled")
            plt.show()

        def __str__(self):
            return (f"Triangle with vertices at "
                    f"({self.point_1.x}, {self.point_1.y}), "
                    f"({self.point_2.x}, {self.point_2.y}), and "
                    f"({self.point_3.x}, {self.point_3.y})")

    # Ejemplo de uso
    if __name__ == "__main__":
        p1 = Point(0.0, 0.0)
        p2 = Point(1.0, 0.0)
        p3 = Point(0.0, 1.0)
        triangle = Triangle(p1, p2, p3)


