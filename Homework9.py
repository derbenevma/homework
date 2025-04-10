# №1
import math

class Shape:
    def area(self):
      raise NotImplementedError("Area calculation is not defined for this shape.")

    def perimeter(self):
      raise NotImplementedError("Perimeter calculation is not defined for this shape.")

class Circle(Shape):
    def __init__(self, radius, fill = None):
        self.radius = radius
        self.fill = fill
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def color(self):
      return self.fill

class Rectangle(Shape):
    def __init__(self, width, height, fill = None):
        self.width = width
        self.height = height
        self.fill = fill
    def area(self):
      return self.width * self.height

    def perimeter(self):
      return 2 * (self.width + self.height)
    
    def color(self):
      return self.fill


circle_1 = Circle(5, 'Red')
print("Circle area:", circle_1.area())
print("Circle perimeter:", circle_1.perimeter())
print("Circle color:", circle_1.color())

rectangle_1 = Rectangle(4, 6, "Green")
print("Rectangle area:", rectangle_1.area())
print("Rectangle perimeter:", rectangle_1.perimeter())
print("Rectangle color:", rectangle_1.color())

circle_2 = Circle(2.5, "Black")
print("Circle 2 area:", circle_2.area())
print("Circle 2 perimeter:", circle_2.perimeter())
print("Circle color:",circle_2.color())

rectangle_2 = Rectangle(7, 3, "Blue")
print("Rectangle 2 area:", rectangle_2.area())
print("Rectangle 2 perimeter:", rectangle_2.perimeter())
print("Rectangle color:", rectangle_2.color())

# №2
class Animal:
  def sound(self):
    return ""

class Dog(Animal):
  @property
  def sound(self):
    return "Гав-Гав"

class Cat(Animal):
  @property
  def sound(self):
    return "Мяу"

class Cow(Animal):
  @property
  def sound(self):
    return "Муу"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
  print(animal.sound)
