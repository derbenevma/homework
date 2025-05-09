# задача 1
# def acos(x, y) :
#     return x  / ((x * x + y * y) ** 0.5)
 
# x1, x2 = map(float,input().split())
# y1, y2 = map(float,input().split())
# z1, z2 = map(float,input().split())
# dot = [x1, x2]
# acosx = acos(x1, x2)
# acosy = acos(y1, y2)
# acosz = acos(z1, z2)
# if acosy > acosx :
#     acosx = acosy
#     dot = [y1, y2]
# if acosz > acosx :
#     acosz = acosz
#     dot = [z1, z2]
# print(*dot)
# задача 2
# n = int(input())
 
# lst = [True for _ in range(n+1)]
 
# i = 1
# while 2*i*(i + 1) < n:
#     j = i
#     while j <= (n - i) / (2*i + 1):
#         lst[2*i*j + i + j] = False
#         j = j + 1
#     i = i + 1
 
# for i in range(1, n+1):
#     elem = lst[i]
#     if elem:
#         prime = 2*i + 1
#         if prime > n: break
#         a = bin(prime)[2:]
#         b = bin(prime)[2:][::-1]
 
#         if a == b:
#             print(prime, end=' ')