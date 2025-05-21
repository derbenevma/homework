#№1
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"


class Point3D(Point2D):
    __slots__ = ('x', 'y', '_z')

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):

        raise AttributeError("Нельзя изменить координату z.")

    def __repr__(self):

        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"



pt2 = Point2D(10, 20)
print(f"Point2D: {pt2}")
pt2.extra = 100  
print(f"Point2D with extra attribute: {pt2.extra}")
print(f"Point2D.__dict__: {pt2.__dict__}") 

pt3 = Point3D(10, 20, 30)
print(f"Point3D: {pt3}")
print(f"x: {pt3.x}, y: {pt3.y}, z: {pt3.z}")


pt3.z = 40
pt3.extra = 100

#№2
import sys
import timeit


class NormalPoint:
 
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def move(self, dx, dy):

        self.x += dx
        self.y += dy


class SlotPoint:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def move(self, dx, dy):

        self.x += dx
        self.y += dy


def performance_comparison(num_iterations=100000):

    normal_point = NormalPoint(1, 2)
    slot_point = SlotPoint(3, 4)

    normal_time = timeit.timeit(
        lambda: normal_point.move(0.1, 0.2),
        number=num_iterations
    )

    slot_time = timeit.timeit(
        lambda: slot_point.move(0.1, 0.2),
        number=num_iterations
    )

    print(f"NormalPoint: {normal_time:.6f} seconds")
    print(f"SlotPoint:   {slot_time:.6f} seconds")


def memory_comparison():
    normal_point = NormalPoint(1, 2)
    slot_point = SlotPoint(3, 4)

    normal_size = sys.getsizeof(normal_point)
    slot_size = sys.getsizeof(slot_point)

    print(f"NormalPoint size: {normal_size} bytes")
    print(f"SlotPoint size:   {slot_size} bytes")



print("Performance Comparison:")
performance_comparison()

print("\nMemory Comparison:")
memory_comparison()

#№3
class Student:
    __slots__ = ('name', 'age', 'grade')

    def __init__(self, name, age, grade):
        if not isinstance(grade, (int, float)):
            raise TypeError("Оценка должна быть числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if grade < 0:
            raise ValueError("Оценка не может быть отрицательной.")

        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"


def calculate_average_grade(students):
    if not students:
        return None

    total_grade = sum(student.grade for student in students)
    return total_grade / len(students)



students = [
    Student("Alice", 20, 4.5),
    Student("Bob", 22, 3.8),
    Student("Charlie", 21, 4.2),
    Student("David", 19, 4.9)
]

average_grade = calculate_average_grade(students)

if average_grade is not None:
    print(f"Средняя оценка студентов: {average_grade:.2f}")
else:
    print("Нет данных о студентах.")

#№4
class Product:

    __slots__ = ('name', 'price', 'quantity')

    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой.")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть целым числом.")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


def find_products_above_threshold(products, price_threshold):
    expensive_products = [name for name, product in products.items() if product.price > price_threshold]
    return expensive_products



products = {
    "Laptop": Product("Laptop", 1200.00, 10),
    "Keyboard": Product("Keyboard", 75.50, 50),
    "Mouse": Product("Mouse", 25.00, 100),
    "Monitor": Product("Monitor", 300.00, 25)
}

threshold = 100.00
expensive_products = find_products_above_threshold(products, threshold)

print(f"Товары с ценой выше {threshold:.2f}:")
for product_name in expensive_products:
    print(f"- {product_name}")

product = Product("Tablet", "800", 15)
product = Product("Phone", 500, -5) 
