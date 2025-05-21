class Fraction:

    _instances = {}  

    def __new__(cls, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен 0.")
        gcd_val = Fraction._gcd(numerator, denominator)
        numerator //= gcd_val
        denominator //= gcd_val
        key = (numerator, denominator)

        if key in cls._instances:
            return cls._instances[key]
        else:
            instance = super().__new__(cls)
            instance.numerator = numerator
            instance.denominator = denominator
            cls._instances[key] = instance
            return instance

    def __init__(self, numerator, denominator):
        if not hasattr(self, 'numerator'):
            if denominator == 0:  # Проверка на 0 теперь только в __new__
                raise ValueError("Знаменатель не может быть равен 0.")

            gcd_val = Fraction._gcd(numerator, denominator)
            self.numerator = numerator // gcd_val
            self.denominator = denominator // gcd_val


    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = Fraction(2, 4)
f4 = Fraction(3, 4)
f5 = Fraction(1, 3)

print(f"f1: {f1}")
print(f"f2: {f2}")
print(f"f3: {f3}")

print(f"f1 == f2: {f1 == f2}")
print(f"f1 == f4: {f1 == f4}")
print(f"f1 == f3: {f1 == f3}")

print(f"f1 is f2: {f1 is f2}")
print(f"f1 is f3: {f1 is f3}")

print(f"f1 < f4: {f1 < f4}")
print(f"f1 <= f2: {f1 <= f2}")
print(f"f1 > f5: {f1 > f5}")
print(f"f1 >= f5: {f1 >= f5}")


f6 = Fraction(1, 0)
