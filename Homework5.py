# № 1 
class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError("Числитель должен быть целым числом.")
        if not isinstance(denominator, int):
            raise TypeError("Знаменатель должен быть целым числом.")
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")

        self._numerator = numerator
        self._denominator = denominator
        self._reduce()  # Упрощаем дробь при создании

    def _reduce(self):
        gcd = Fraction.gcd(abs(self._numerator), abs(self._denominator))
        self._numerator //= gcd
        self._denominator //= gcd
        # Убеждаемся, что отрицательный знак стоит в числителе (или дробь положительна)
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @classmethod
    def from_float(cls, float_value):
        integer_part = int(float_value)
        decimal_part = float_value - integer_part
        if decimal_part == 0:
            return cls(integer_part, 1)
        denominator = 1
        while decimal_part != int(decimal_part):
            decimal_part *= 10
            denominator *= 10
            
        numerator = int(float_value * denominator)
        return cls(numerator, denominator)

    @property
    def value(self):
        return round(self._numerator / self._denominator, 3)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator
    

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно складывать только объекты Fraction.")
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно вычитать только объекты Fraction.")
        new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно умножать только объекты Fraction.")
        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Можно делить только объекты Fraction.")
        if other._numerator == 0:
            raise ZeroDivisionError("Деление на ноль!")
        new_numerator = self._numerator * other._denominator
        new_denominator = self._denominator * other._numerator
        return Fraction(new_numerator, new_denominator)
    
    def __float__(self):
         return self.value
    
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self._numerator == other._numerator and self._denominator == other._denominator

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1 + f2)
print(f1 - f2) 
print(f1 * f2)  
print(f1 / f2)  
print(f1.value) 
print(float(f1)) 
f3 = Fraction(2, 4)
print(f1 == f3) 


# № 2 
from fractions import Fraction

class FractionMatrix:
    def __init__(self, matrix):
        self._matrix = [[Fraction(x) for x in row] for row in matrix]
        self._rows = len(self._matrix)
        self._cols = len(self._matrix[0]) if self._rows > 0 else 0

    @property
    def matrix(self):
        return self._matrix

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def __str__(self):
        return "\n".join([" ".join(str(x) for x in row) for row in self._matrix])

    def __add__(self, other):
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")

        result = [[self._matrix[i][j] + other._matrix[i][j] for j in range(self._cols)] for i in range(self._rows)]
        return FractionMatrix(result)

    def __sub__(self, other):
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для вычитания.")

        result = [[self._matrix[i][j] - other._matrix[i][j] for j in range(self._cols)] for i in range(self._rows)]
        return FractionMatrix(result)

    def __mul__(self, other):
        if self._cols != other._rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")

        result = [[sum(self._matrix[i][k] * other._matrix[k][j] for k in range(self._cols)) for j in range(other._cols)] for i in range(self._rows)]
        return FractionMatrix(result)

    def transpose(self):
        result = [[self._matrix[j][i] for j in range(self._rows)] for i in range(self._cols)]
        return FractionMatrix(result)

    @property
    def determinant(self):
        if self._rows != self._cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц.")

        if self._rows == 1:
            return self._matrix[0][0]
        elif self._rows == 2:
            return self._matrix[0][0] * self._matrix[1][1] - self._matrix[0][1] * self._matrix[1][0]
        else:
            det = Fraction(0, 1)
            for j in range(self._cols):
                submatrix = [row[:j] + row[j+1:] for row in self._matrix[1:]]
                sign = Fraction(1, 1) if j % 2 == 0 else Fraction(-1, 1)
                det += sign * self._matrix[0][j] * FractionMatrix(submatrix).determinant
            return det

    @staticmethod
    def check_dimensions(matrix1, matrix2, operation):
        if operation == "addition" or operation == "subtraction":
            if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
                raise ValueError("Матрицы должны иметь одинаковые размеры для сложения/вычитания.")
        elif operation == "multiplication":
            if matrix1.cols != matrix2.rows:
                raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
        elif operation == "determinant":
            if matrix1.rows != matrix1.cols:
                raise ValueError("Определитель можно вычислить только для квадратных матриц.")
        else:
            raise ValueError("Неизвестная операция.")
    
    @classmethod
    def create_identity_matrix(cls, size):
        identity_matrix = [[Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(size)] for i in range(size)]
        return cls(identity_matrix)

    def __new__(cls, matrix):
        if not isinstance(matrix, list):
            raise TypeError("Матрица должна быть представлена в виде списка списков.")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("Каждая строка матрицы должна быть списком.")
        if not all(isinstance(x, (int, Fraction)) for row in matrix for x in row):
            raise TypeError("Все элементы матрицы должны быть целыми числами или дробями.")
        if len(matrix) > 0:
            row_len = len(matrix[0])
            if not all(len(row) == row_len for row in matrix):
                raise ValueError("Все строки матрицы должны иметь одинаковую длину.")

        instance = super().__new__(cls)
        return instance    
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
print("m1:")
print(m1)
print("\nm2:")
print(m2)

print("\nm1 + m2:")
print(m1 + m2)
print("\nm1 * m2:")
print(m1 * m2) 
print("\nОпределитель m1:")
print(m1.determinant) 
print("\nТранспонированная m1:")
print(m1.transpose())
