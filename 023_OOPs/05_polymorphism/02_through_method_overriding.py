class Shape:

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, side: int):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):

    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


# creating an object which stores a list;

shapes = [Rectangle(5, 6), Square(8), Circle(2)]
for shape in shapes:
    print(shape.area())
