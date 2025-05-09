# Задача 1
# import re

# def naity(m):
#   if re.fullmatch(r"\b[ABEKMHOPCTYX]{1}\d{3}[ABEKMHOPCTYX]{2}\s+\d{2,3}\b", m):
#     return "chastny"
#   elif re.fullmatch(r"\b[ABEKMHOPCTYX]{2}\d{3}\s\d{2,3}\b", m):
#     return "taxi"
#   else:
#     return "ne znayu"
# m = input()
# result = naity(m)
# print(result)

# Задача 2
# print (len(re.findall(r"\b[A-Za-zА-Яа-я]+\b", input())))

# Задача 3
# pismo = input()
# poisk = re.findall(r"\b\d{2}\W\d{2}\W\d{2}\b", pismo)
# redakcia = re.sub(r"\b\d{2}\W\d{2}\W\d{2}\b", "TBD", pismo)
# print(redakcia)

# Задача 4
# p = []
# s = input('Введите строку: ')

# abr = ''
# for i in range(len(s)):
#     if ord(s[i]) in range(1040,1072):
#         abr += s[i]
#     elif s[i] == ' ' and i < len(s)-1:
#         if ord(s[i+1]) not in range(1040,1072):
#             if len(abr) > 1:
#                 p.append(abr[1:])
#                 abr = ''
#         else:
#             abr += ' '

# print(p)
