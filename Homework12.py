# №1
# def find_elements_by_index(values, indices):
#     result = []
#     try:
#         for index in indices:
#             result.append(values[index])
#         return result
#     except IndexError as e:
#         return f"Ошибка индекса: {e}"
  
# values = [10, 20, 30, 40, 50]
# indices = [1,2]
# result = find_elements_by_index(values, indices)
# print(result)


#№2
# import math

# class Circle:

#     def __init__(self, radius):

#         self.radius = radius

     @property
#     def diameter(self):

#         return 2 * self.radius

#     @diameter.setter
#     def diameter(self, new_diameter):

#          self.radius = new_diameter / 2

#     def area(self):

#         return math.pi * self.radius**2

# my_circle = Circle(radius=5)

# print(f"Радиус круга: {my_circle.radius}")
# print(f"Диаметр круга: {my_circle.diameter}")
# print(f"Площадь круга: {my_circle.area()}")

# my_circle.diameter = 12
# print(f"Радиус круга после изменения диаметра: {my_circle.radius}")
