# from datetime import datetime

# class Book:

#     def __init__(self, title, author, year):
#         if not Book._is_valid_year(year):
#             raise ValueError("Year must be an integer and not in the future.")

#         self.__title = title
#         self.__author = author
#         self.__year = year

#     def get_info(self):
#         return f"{self.__title}, автор: {self.__author}, год: {self.__year}"

#     @staticmethod
#     def _is_valid_year(year):
#         current_year = datetime.now().year
#         return isinstance(year, int) and year <= current_year

#     @classmethod
#     def create_default_year(cls, title, author):
#         return cls(title, author, 2024)

# book1 = Book("1984", "George Orwell", 1949)
# print(book1.get_info())

# book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
# print(book2.get_info())
