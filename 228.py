import math

class Shape:
    def area(self):
        raise NotImplementedError("Area calculation is not defined for this shape.")

    def perimeter(self):
        raise NotImplementedError("Perimeter calculation is not defined for this shape.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Example Usage:
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

# Additional examples
circle2 = Circle(2.5)
print("Circle 2 area:", circle2.area())
print("Circle 2 perimeter:", circle2.perimeter())

rectangle2 = Rectangle(7, 3)
print("Rectangle 2 area:", rectangle2.area())
print("Rectangle 2 perimeter:", rectangle2.perimeter())