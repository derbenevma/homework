class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Сегодня мы готовим {self.name}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
        print(f"Блюдо {self.name} готово!")

spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()

# 3. Класс "Кэширующий калькулятор"
class CacheCalculator:
    def __init__(self):
        self._cache = {}

    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Аргумент должен быть числом")

        if x not in self._cache:
            self._cache[x] = x * x

        return self._cache[x]

    @property
    def cache(self):
        return self._cache

# Примеры проверки (раскомментируйте, чтобы протестировать)
# calc = CacheCalculator()
# calc(2)  # 4, кэш {2:4}
# calc(2.5)  # 6.25, кэш {2:4, 2.5:6.25}
# calc("text")  # TypeError
# print(calc.cache)  # {'2':4, ...}
