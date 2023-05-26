class Figure:
    unit = 'cm'

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

    def info(self):
        area = self.calculate_area()
        print(f"Circle radius: {self.__radius}{Figure.unit}, area: {area:.2f}{Figure.unit}")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{Figure.unit}, side b: {self.__side_b}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}")


circle1 = Circle(2)
circle2 = Circle(3)

triangle1 = RightTriangle(5, 8)
triangle2 = RightTriangle(3, 4)
triangle3 = RightTriangle(6, 9)

figures = [circle1, circle2, triangle1, triangle2, triangle3]

for figure in figures:
    figure.info()
