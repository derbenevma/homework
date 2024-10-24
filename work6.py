# Задача 1
# import random
# matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
# print('Исходная матрица:',matrix)
# s=[]
# for i in range(len(matrix)):
#     s.append(sum(matrix[i]))
# print("Строка с наибольшей суммой:",matrix[s.index(max(s))],"Сумма элементов:",max(s),"Строка с наименьшей суммой:",matrix[s.index(min(s))],"Сумма элементов:",min(s))
# Задача 2

# from random import randint
 
# N, M = 3, 4
# a = [[randint(-10, 10) for _ in range(M)] for _ in range(N)]
# print(a)
# for i in range(N):
#     for j in range(M):
#         if a[i][j] % 2 == 1 or a[i][j] % 2 == -1:
#             a[i][j] = 1
#         else: a[i][j] = 0
# print(a)