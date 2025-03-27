import matplotlib.pyplot as plt
import numpy as np

class Derivative:

    def __init__(self, func):
        self.func = func
        self.h = 1e-5

    def __get__(self, instance, owner):
        return self  

    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)


class ExponentialFunction:

    def __init__(self, a):
        self.a = a
        self.derivative = Derivative(self)  

    def __call__(self, x):
        return self.a * np.exp(x)

func = ExponentialFunction(2)
x = np.linspace(-2, 2, 100)
y = [func(xi) for xi in x]
dy = [func.derivative(xi) for xi in x]

plt.plot(x, y, label='f(x)')
plt.plot(x, dy, label='f\'(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Экспоненциальная функция и её производная')
plt.legend()
plt.grid(True)
# plt.show()
