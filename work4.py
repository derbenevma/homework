# s = input()
# counter = 0
# N_words = []
# for n, i in enumerate(s):
#     if i == 'н':
#         if counter == 0:
#             N_words.append([n])
#         counter += 1
#     elif i != 'н' and counter > 0:
#         N_words[-1].append(counter)
#         counter = 0
# else:
#     if counter > 0:
#         N_words[-1].append(counter)
# N_words = sorted(N_words, key=lambda x: x[1], reverse=True)
# t = '!' * N_words[0][1]
# s = s[:N_words[0][0]] + t + s[N_words[0][0]+N_words[0][1]+1:]
# print(s)
# print(f'количество н: {N_words[0][1]}')
# # Задача 2
# s = input() 
# print(s[s.index('(')+1:s.index(')')])
# Задача 3
# s = input()
# in_я = []
# for n, i in enumerate(s):
#     if i == 'я':
#         for j in range(n, len(s)):
#             if s[j] == 'а' and j - n > 1:
#                 in_я.append([n, j])
# for i in in_я:
#     print(s[i[0]+1:i[1]])