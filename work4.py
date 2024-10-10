# Задача 2
# s = 'dfgsd(gsdfgs)fgsdfgsfgsfg' 
# print(s[s.index('(')+1:s.index(')')])
# Задача 3
# s = 'оврпаоаилоряорягвармяомтряоваяюмяоаврмюявамо'
# in_я = []
# for n, i in enumerate(s):
#     if i == 'я':
#         for j in range(n, len(s)):
#             if s[j] == 'а' and j - n > 1:
#                 in_я.append([n, j])
# for i in in_я:
#     print(s[i[0]+1:i[1]]